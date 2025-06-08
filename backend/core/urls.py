"""Django URL Configuration"""
from core import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token # Default
from .auth import CustomAuthToken


router = DefaultRouter()
router.register(r'accounts', views.AccountViewsets, basename='account')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),

    # path('auth-token', obtain_auth_token),
    path('auth-token', CustomAuthToken.as_view()),
]