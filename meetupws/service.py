from django.conf import settings

import meetup.api


class MeetupService:
    """
    Service for Meetup.com API integration

    TODO: complete service implementation according to API endpoint requirements
    """

    def __init__(self):
        self.token = settings.MEETUPCOM_OAUTH_TOKEN
        self.client = meetup.api.Client(self.token)

    @staticmethod
    def _create_request_config(required: dict, params=None) -> dict:
        """
        Create Meetup.com API request configuration

        :param required: the required URL parameter(s)
        :param params: the optional URL parameter(s)
        :return: request parameter dictionary
        """

        config = required.copy()
        if params:
            config.update(params)

        return config

    def get_meetup_group(self, url_name: str, params=None) -> dict:
        """
        GET https://api.meetup.com/:urlname?params

        :param url_name: the urlname param string
        :param params: optional URL parameters
        :return: Meetup.com API response or {}
        """

        try:
            return self.client.GetGroup(self._create_request_config(required={'urlname': url_name}, params=params))
        except Exception as e:
            return {'Exception': str(e)}

    def get_meetup_events(self, url_name: str, params=None) -> dict:
        """
        GET https://api.meetup.com/:urlname/events?params

        :param url_name: the urlname param string
        :param params: optional URL parameters
        :return: Meetup.com API response or {}
        """

        try:
            return self.client.GetEvents(self._create_request_config(required={'urlname': url_name}, params=params))
        except Exception as e:
            return {'Exception': str(e)}
