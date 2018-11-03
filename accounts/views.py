from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountList(ListAPIView):
    """
    List all registered user accounts
    """

    permission_classes = (IsAdminUser,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountRegister(APIView):
    """
    Register for a new user account
    """

    permission_classes = (AllowAny,)

    def post(self, req):
        account = Account()
        serializer = AccountSerializer(account, data=req.data)
        if serializer.is_valid():
            serializer.password = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST, data={
            'reason': 'Request data not properly structured'
        })


class AccountLogin(APIView):
    """
    Login a registered user account
    """

    permission_classes = (AllowAny,)

    def post(self, req):
        if not req.data:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'reason': 'Authentication data not provided (username, email)'
            })

        try:
            account = Account.objects.get(username=req.data['username'], email=req.data['email'])
        except KeyError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'reason': 'Key %s not found in request data' % str(e)
            })
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'reason': 'Account not found'
            })

        if account:
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(account)
            jwt_token = jwt_encode_handler(payload)

            return Response(status=status.HTTP_200_OK, data={
                'token': jwt_token
            })
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'reason': 'Could not verify account information'
            })


class AccountDetails(APIView):
    """
    Retrieve/update the requested user account information
    """

    permission_classes = (IsAuthenticated,)

    def get(self, req, pk):
        if req.user.pk != int(pk) and not req.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'reason': 'User account is not authorized'
            })

        try:
            acc = Account.objects.get(id=pk)
            serializer = AccountSerializer(instance=acc)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'reason': 'User account not found for the requested pk'
            })

        if req.user.is_superuser:
            acc_data = serializer.data
        else:
            acc_data = {
                'id': serializer.data['id'],
                'username': serializer.data['username'],
                'first_name': serializer.data['first_name'],
                'last_name': serializer.data['last_name'],
                'email': serializer.data['email'],
                'profile_pic': serializer.data['profile_pic']
            }

        return Response(status=status.HTTP_202_ACCEPTED, data=acc_data)

    def patch(self, req, pk):
        if req.user.pk != int(pk) and not req.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={
                'reason': 'User account is not authorized'
            })

        try:
            acc = Account.objects.get(id=pk)
            serializer = AccountSerializer(acc, data=req.data, partial=True)
            if serializer.is_valid():
                serializer.save()
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND, data={
                'reason': 'User account not found for the requested pk'
            })

        if req.user.is_superuser:
            acc_data = serializer.data
        else:
            acc_data = {
                'id': serializer.data['id'],
                'username': serializer.data['username'],
                'first_name': serializer.data['first_name'],
                'last_name': serializer.data['last_name'],
                'email': serializer.data['email'],
                'profile_pic': serializer.data['profile_pic']
            }

        return Response(status=status.HTTP_202_ACCEPTED, data=acc_data)


class AccountSetup(APIView):
    """
    Set up user Account password after initial registration
    """

    permission_classes = (AllowAny,)

    def get(self, req, pk, key):
        try:
            acc = Account.objects.get(pk=pk)

            if acc is None or acc.init_pass is None or acc.init_pass.hex != key:
                return Response(status=status.HTTP_403_FORBIDDEN, data={
                    'reason': 'User account is not authorized'
                })

            return Response(status=status.HTTP_200_OK)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, req, pk, key):
        try:
            acc = Account.objects.get(pk=pk)

            if acc is None or acc.init_pass is None or acc.init_pass.hex != key:
                return Response(status=status.HTTP_403_FORBIDDEN)

            if req.data['pass'] != req.data['pass_repeat']:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={
                    'reason': 'Password values do not match.'
                })

            acc.password = make_password(req.data['pass'])
            acc.init_pass = None
            acc.save()

            return Response(status=status.HTTP_202_ACCEPTED)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
