from rest_framework import serializers
from .models import Account
from datetime import datetime

""" -------------- Serializer Fields -----------------.
name =  serializers.CharField(min_length=3, 
        max_length=5, 
        allow_null=True,  # Instead of allow_null use `allow_blank`
        allow_blank=True, 
        trim_whitespace=True)

UUIDField()
IntegerField()
FloatField()
DecimalField()
SlugField()
EmailField()
BooleanField()
URLField()
FileField()
FilePathField()
ImageField()
DateField()
TimeField()
DateTimeField()
DurationField()
IPAddressField()
ChoiceField()
MultipleChoiceField()
ListField()
DictField()
JSONField()
"""

""" -------------- Core Arguments --------------

-label
-style
-validators
-error_messages
-help_text
-required
-default
-read_only=False [default]
-write_only=True [default]
-allow_null
"""


class AccountSerializer(serializers.Serializer):
    # id = serializers.CharField(max_length=50, read_only=True) # For UUID
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    bank = serializers.ChoiceField(choices=Account.BANK_CHOICES, default='Other')
    account_number = serializers.CharField(max_length=20)
    balance = serializers.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created_at = serializers.DateTimeField(read_only=True)
