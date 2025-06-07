from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class AccountView(View):
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            account = Account.objects.get(id=pk)
            serializer = AccountSerializer(account)
            python_data = serializer.data
            return JsonResponse(python_data)
        
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        python_data = serializer.data
        return JsonResponse(python_data, safe=False)

    def post(self, request, pk=None, *args, **kwargs):
        if pk is None:
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = AccountSerializer(data = python_data)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account added successfully."}
                return JsonResponse(res)
            return JsonResponse(serializer.errors)

    def patch(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            account = Account.objects.get(id=pk)
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = AccountSerializer(account, data = python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account partially updated successfully."}
                return JsonResponse(res)
            return JsonResponse(serializer.errors)

    def put(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            account = Account.objects.get(id=pk)
            json_data = request.body
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = AccountSerializer(account, data = python_data)
            if serializer.is_valid():
                serializer.save()
                res = {"success":True, "message":"Account fully updated successfully."}
                return JsonResponse(res)
            return JsonResponse(serializer.errors)

    def delete(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            account = Account.objects.get(id=pk)
            account.delete()
            res = {"success":True, "message":"Account deleted successfully."}
            return JsonResponse(res)