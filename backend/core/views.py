from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class AccountViewsets(viewsets.ViewSet):
    def list(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        account = get_object_or_404(Account, id=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = AccountSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success":True, "message":"Account added successfully."}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        account = get_object_or_404(Account, id=pk)
        serializer = AccountSerializer(account, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"success":True, "message":"Account partially updated successfully."}
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        account = get_object_or_404(Account, id=pk)
        serializer = AccountSerializer(account, data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"success":True, "message":"Account fully updated successfully."}
            return Response(res)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        account = get_object_or_404(Account, id=pk)
        account.delete()
        res = {"success":True, "message":"Account deleted successfully."}
        return Response(res)