from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer

# Create your views here.


def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    print('-'*100)
    python_data = serializer.data
    print(f"Python data : {python_data}")
    print('-'*100)
    return JsonResponse(python_data, safe=False)


def account_view(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account)
    print('-'*100)
    python_data = serializer.data
    print(f"Python data : {python_data}")
    print('-'*100)

    return JsonResponse(python_data)
