"""bundle_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.conf.urls import url
# from .auth.views import AuthView
# from .user.views import UserView, UserSettings

urlpatterns = [

    # url('users/current', UserView.as_view(), name='Current user'),
    # url('auth/login', AuthView.login, name='User login'),
    # url('auth/sign-up', AuthView.sign_up, name='Sign up a new user'),
    # url('auth/request-pass', AuthView.request_pass, name='Send an email with password'),
    # url('auth/reset-pass', AuthView.reset_pass, name='Reset a pasword'),
    # url('auth/sign-out', AuthView.sign_out, name='Sign out'),
    # url('settings/current', UserSettings.as_view(), name='User settings'),
]

# from django.conf.urls import url
# from django.urls import path
# from rest_framework import routers
# from django.conf.urls import include
# from .views import OrganisationViewSet, RatingViewSet, UserViewSet
# from .user.views import UserView

# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('organisations', OrganisationViewSet)
# router.register('ratings', RatingViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     url('users/current', UserView.as_view(), name='Current user'),
# ]
