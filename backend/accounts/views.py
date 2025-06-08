from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from django.contrib.auth import authenticate

class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'success':True, 'message':'Registration successfuly.'}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                res = {'success':True, 'message':'Login successfuly.'}
                return Response(res, status=status.HTTP_200_OK)
            errors = {'errors': {'non_field_errors': ['User not found']}}
            return Response(errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

