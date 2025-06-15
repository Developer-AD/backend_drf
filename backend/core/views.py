from .models import Account
from .serializers import AccountSerializer
from rest_framework import status, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# from .filters import AccountFilter


# Create your views here.
class AccountViewsets(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    # queryset = Account.objects.filter(bank='HDFC')
    # queryset = Account.objects.filter(bank='SBI')
    serializer_class = AccountSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    

    # def get_queryset(self):
    #     return Account.objects.filter(user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def get_queryset(self):
    #     print('-'*100)
    #     params = self.request.query_params
    #     print(f"params : ", params)
    #     bank = params.get('bank')
    #     print(f"bank - {bank}, & type : {type(bank)}")
    #     # queryset = Account.objects.filter(bank='SBI')
    #     queryset = Account.objects.filter(user=self.request.user)
    #     # queryset = Account.objects.all()
    #     if bank is not None:
    #         queryset = queryset.filter(bank=bank)

    #     print('-'*100)
    #     return queryset

    # -------------------- Equally based filter ----------------
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bank', 'user']

    # http://localhost/api/accounts/?bank=HDFC
    # http://localhost/api/accounts/?user=3
