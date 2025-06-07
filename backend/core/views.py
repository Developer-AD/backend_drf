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
    print(f"Python data : {python_data}")
    print('-'*100)

    # with JsonResponse we can skip this two lines.
    # json_data = JSONRenderer().render(python_data)
    # return HttpResponse(json_data, 'application/json')

    # # safe=True [default] it will only send dict data type.
    # # safe=False we have to change this for sending other types like list of dict.
    # return JsonResponse(python_data)
    
    return JsonResponse(python_data, safe=False)


def account_view(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account)
    print('-'*100)
    python_data = serializer.data
    print(f"Python data : {python_data}")
    print('-'*100)

    # with JsonResponse we can skip this two lines.
    # json_data = JSONRenderer().render(python_data)
    # return HttpResponse(json_data, 'application/json')
    return JsonResponse(python_data)
