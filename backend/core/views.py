from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class AccountView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success":True, "message":"Account added successfully."}
            return Response(res, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account partially updated successfully."}
                return Response(res)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account, data = request.data)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account fully updated successfully."}
                return Response(res)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            account.delete()
            res = {"success":True, "message":"Account deleted successfully."}
            return Response(res)