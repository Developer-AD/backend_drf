"""Django URL Configuration"""
from core import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewsets, basename='account')


urlpatterns = [
    path('', include(router.urls)),
    path('ws/', views.websocket),
]