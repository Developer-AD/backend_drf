from .models import Account
from .serializers import AccountSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def account_view(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        if pk is None:
            serializer = AccountSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account added successfully."}
                return Response(res, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account, data = request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account partially updated successfully."}
                return Response(res)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            serializer = AccountSerializer(account, data = request.data)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account fully updated successfully."}
                return Response(res)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if pk is not None:
            account = get_object_or_404(Account, id=pk)
            account.delete()
            res = {"success":True, "message":"Account deleted successfully."}
            return Response(res)