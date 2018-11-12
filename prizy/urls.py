"""prizy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    # JWT authentication
    path('auth/', obtain_jwt_token, name='jwt_auth'),
    path('refresh/', refresh_jwt_token, name='jwt_refresh'),
    path('verify/', verify_jwt_token, name='jwt_verify'),
    # API routes
    path('api/', include('accounts.urls')),
    path('api/', include('events.urls')),
]

# Defining where the images are placed, for DEBUG mode only!!!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
