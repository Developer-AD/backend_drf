from rest_framework import serializers
from .models import Account
from datetime import datetime

class AccountSerializer(serializers.Serializer):
    # id = serializers.CharField(max_length=50, read_only=True) # For UUID
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    bank = serializers.ChoiceField(choices=Account.BANK_CHOICES)
    account_number = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = serializers.DateTimeField(read_only=True)


    # Deserialization
    def create(self, validated_data):
        return Account.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print('-'*100)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        #     print(f"Att: {attr} - {value}")
        # print(f"Initial data : {instance}")
        # print(f"Validated data : {validated_data}")
        # instance.name = validated_data.get('name', instance.name)
        # instance.bank = validated_data.get('bank', instance.bank)
        # instance.account_number = validated_data.get('account_number', instance.account_number)
        # instance.description = validated_data.get('description', instance.description)
        # instance.balance = validated_data.get('balance', instance.balance)
        instance.save()

        # for attr, value in validate_data

        print('-'*100)
        return instance
