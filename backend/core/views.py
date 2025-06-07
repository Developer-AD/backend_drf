from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Account
from .serializers import AccountSerializer

from rest_framework.renderers import JSONRenderer

# Create your views here.


def account_list(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    print('-'*100)
    python_data = serializer.data
    json_data = JSONRenderer().render(python_data)

    print(f"Python data : {python_data}")
    print(f"JSON data : {json_data}")
    print('-'*100)
    return HttpResponse(json_data, 'application/json')


def account_view(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account)
    print('-'*100)
    python_data = serializer.data
    json_data = JSONRenderer().render(python_data)

    print(f"Python data : {python_data}")
    print(f"JSON data : {json_data}")
    print('-'*100)
    # return HttpResponse(json_data) # This is send json data as text. 
    return HttpResponse(json_data, 'application/json') # Send data in json format.