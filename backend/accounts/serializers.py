from rest_framework import serializers
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        """ You will get only that fields that you mention here in your API """
        model = MyUser

        fields = ['id', 'full_name', 'username', 'password', 'password2', 'role', 'gender', 'contact_no']

        extra_kwargs = {
            'password':{'write_only':True},
            'id':{'read_only':True}
        }
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return data
    
    def create(self, validated_data):
        # validated_data.pop('password2')
        # return MyUser.objects.create_user(**validated_data)
        username = validated_data.get('username')
        password = validated_data.get('password')
        full_name = validated_data.get('full_name')
        role = validated_data.get('role')
        return MyUser.objects.create_user(username=username, password=password,
                                          full_name=full_name, role=role)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)