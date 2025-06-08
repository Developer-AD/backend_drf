from rest_framework.authentication import BaseAuthentication
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed


MyUser = get_user_model()

class CustomAuth(BaseAuthentication):
    def authenticate(self, request):
        # http://localhost/api/accounts/?username=abhishek 
        # To test this you have to send your username as a query parameter.
        username = request.GET.get('username')
        if username is None:
            return None

        try:
            user = MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            raise AuthenticationFailed("No such user.")
        return (user, None)