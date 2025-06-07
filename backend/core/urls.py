"""Django URL Configuration"""
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', views.AccountViewsets, basename='account')
urlpatterns = router.urls