from .models import Account
from .serializers import AccountSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


# Create your views here.
# You can use anythings either long fn to create views or 3 lines
# Authentication will work same as it is.
class AccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny] # Same as without login.