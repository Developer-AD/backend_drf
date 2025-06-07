from rest_framework import serializers
from .models import Account
import re

class AccountSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    # Priority:- Validators > Field Level Validation > Object Level Validation
    # 1. Validators : Validate name: only letters (a-z, A-Z) and spaces
    # This single validators can be used in multiple fields and in one field we can use multiple validators.

    # To implement validators in ModelSerializer we have to override the field.

    def no_special_chars(value):
        if not re.fullmatch(r"[A-Za-z ]+", value):
            raise serializers.ValidationError(
                "Name can contain only alphabets and spaces")
        return value

    name = serializers.CharField(max_length=100, validators=[no_special_chars])



    class Meta:
        """ You will get only that fields that you mention here in your API """
        model = Account

        fields = ['id', 'name', 'bank', 'description', 'account_number', 'balance', 'created_at']
        # read_only_fields = ['id', 'created_at', 'updated_at']

        # 'write_only' - It will not visible in view just we can update it.
        # extra_kwargs = {'created_at': {'read_only': True}}

        # fields = '__all__' # Include all fields.
        # exclude = ['updated_at', 'is_deleted'] # Include all fields except this.

    # No need to implement create() and update().



    # 2. Field Level Validation : When you have one field to validate.
    # def validate_balance(self, value):
    #     if value < 0:
    #         raise serializers.ValidationError("Amount balance must be positive.")
    #     return value

    # 3. Object Level Validation : When you have more fields to validate.
    # def validate(self, data):
    #     balance = data.get('balance')
    #     name = data.get('name')
    #     print(f"balance : {balance}")
    #     print(f"name : {name}")

    #     # Validate balance
    #     if balance < 0:
    #         raise serializers.ValidationError(
    #             "Amount balance must be positive.")

    #     # Validate name: only letters (a-z, A-Z) and spaces
    #     if not re.fullmatch(r"[A-Za-z ]+", name):
    #         raise serializers.ValidationError("Name can contain only alphabets and spaces")

    #     return data

