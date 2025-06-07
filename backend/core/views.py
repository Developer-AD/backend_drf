from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class AccountReadOnlyModelViewsets(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer