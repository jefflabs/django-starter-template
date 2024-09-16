"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

# from app_users.views import profile_view
from app_home.views import *
from app_users.views import profile_view

from decouple import config
ADMIN_URL = config("ADMIN_URL", default='admin') 

urlpatterns = [
    path(f'{ADMIN_URL}/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    # path('users/', include(('app_users.urls','users'),namespace='users')), 

    path('', include('app_home.urls')),
    path('profile/', include('app_users.urls')),
    path('@<username>/', profile_view, name="profile"),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)