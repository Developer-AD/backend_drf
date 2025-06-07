from rest_framework import serializers
from .models import Account
from datetime import datetime

class AccountSerializer(serializers.Serializer):
    # id = serializers.CharField(max_length=50, read_only=True) # For UUID
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    bank = serializers.ChoiceField(choices=Account.BANK_CHOICES, default='Other')
    account_number = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = serializers.DateTimeField(read_only=True)


    # Deserialization
    def create(self, validated_data):
        return Account.objects.create(**validated_data)
