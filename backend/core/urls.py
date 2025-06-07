"""Django URL Configuration"""

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('accounts', views.AccountView.as_view()),
    path('accounts/<int:pk>', views.AccountView.as_view()),
]