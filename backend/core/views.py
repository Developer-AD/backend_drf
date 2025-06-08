from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.

"""
# from rest_framework.authentication import SessionAuthentication
# rest_frameworks browsable api uses Session Authentication
# Basic authentication/logout may be not worked.
"""

class AccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
    # permission_classes = [AllowAny] # Same as without login.