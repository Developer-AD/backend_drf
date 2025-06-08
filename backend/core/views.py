from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

"""
# from rest_framework.authentication import SessionAuthentication
# rest_frameworks browsable api uses Session Authentication
# Basic authentication/logout may be not worked.
"""

class AccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]