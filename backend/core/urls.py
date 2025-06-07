"""Django URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('accounts/', views.account_list),
    path('accounts/<int:pk>', views.account_view),
]