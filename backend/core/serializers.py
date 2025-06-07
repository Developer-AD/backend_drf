from rest_framework import serializers
from .models import Account
import re

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        """ You will get only that fields that you mention here in your API """
        model = Account

        fields = ['id', 'name', 'bank', 'description', 'account_number', 'balance', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_name(self, value):
        if not re.fullmatch(r"[A-Za-z ]+", value):
            raise serializers.ValidationError(
                "Name can contain only alphabets and spaces")
        return value