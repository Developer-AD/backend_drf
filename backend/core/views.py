from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    python_data = serializer.data
    return JsonResponse(python_data, safe=False)


def account_view(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account)
    python_data = serializer.data
    return JsonResponse(python_data)


@csrf_exempt
def account_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = AccountSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {"success":True, "message":"Data Created"}
            return JsonResponse(res)
        return JsonResponse(serializer.errors)
