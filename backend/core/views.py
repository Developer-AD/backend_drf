from .models import Account
from .serializers import AccountSerializer
from rest_framework import status, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from .filters import AccountFilter

from django.http import HttpResponse
from django.shortcuts import render, redirect

# ------------- Import custom paginations ------------.
from .paginations import CustomPageNumPagination, CustomLimitOffset, CustomCursor


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
    # filterset_fields = ['bank', 'user', 'name']

    # http://localhost/api/accounts/?bank=HDFC
    # http://localhost/api/accounts/?user=3

    # -------------------- SearchFilter ----------------
    # filter_backends = [SearchFilter]
    # search_fields = ['name'] # single field search
    # search_fields = ['name', 'bank', 'account_number'] # MultiField search.

    # http://localhost/api/accounts/?search=testing  # filter based on icontains
    # Prefix	        Lookup	
    # ^	istartswith	    Starts-with search.
    # =	iexact	        Exact matches.
    # $	iregex	        Regex search.
    # @	search	        Full-text search (Currently only supported Django's PostgreSQL backend).
    # None	            icontains

    # search_fields = ['name'] # Default icontains.
    # search_fields = ['name', '=bank']

    # ------- Change search -- q
    # 'SEARCH_PARAM':'search' # default.
    # 'SEARCH_PARAM':'q' # Add in settings.
    # http://localhost/api/accounts/?q=other


    # -------------------- OrderingFilter ----------------
    # filter_backends = [OrderingFilter]

    # Without ordering_fields we can order by all fields.
    # http://localhost/api/accounts/?ordering=id  # Ascending
    # http://localhost/api/accounts/?ordering=-id # Descending

    # http://localhost/api/accounts/?ordering=-id

    # ordering_fields = ['id', 'created_at', 'bank']


    # ============================ Pagination ============================
    """
    1. PageNumberPagination
    2. LimitOffsetPagination
    3. CursorPagination
    """
    # 1. PageNumberPagination
    # http://localhost/api/accounts/?page=3

    # pagination_class = CustomPageNumPagination

    # 2. LimitOffsetPagination
    # http://localhost/api/accounts/?limit=3&offset=5
    # pagination_class = CustomLimitOffset


    # 3. CustomCursor
    """
        Cursor Pagination : - Mostly Blog Post has this pagination.
        Prev & Next only.
        field='created' [timestamp] it expect you have this field in the model else get error.


    """
    pagination_class = CustomCursor


def websocket(request):
    return render(request, 'websocket.html')