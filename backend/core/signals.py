from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from decimal import Decimal
from .models import *


# --------------------------- Handle Income Automatically --------------------------
# @receiver(post_save, sender=Income)
# def update_account_balance_on_income(sender, instance, created, **kwargs):
#     def update_balance():
#         account = instance.account
#         amount = Decimal(str(instance.amount)) if not isinstance(
#             instance.amount, Decimal) else instance.amount

#         if created:
#             account.balance += amount
#             account.save()

#     transaction.on_commit(update_balance)


# @receiver(post_delete, sender=Income)
# def deduct_account_balance_on_income_delete(sender, instance, **kwargs):
#     def deduct_balance():
#         account = instance.account
#         account.balance -= instance.amount
#         account.save()

#     transaction.on_commit(deduct_balance)


# # --------------------------- Handle Expenses Automatically --------------------------
# @receiver(post_save, sender=Expense)
# def update_account_balance_on_expense(sender, instance, created, **kwargs):
#     def update_balance():
#         account = instance.account
#         amount = Decimal(str(instance.amount)) if not isinstance(
#             instance.amount, Decimal) else instance.amount

#         if created:
#             account.balance -= amount
#             account.save()

#     transaction.on_commit(update_balance)


# @receiver(post_delete, sender=Expense)
# def add_account_balance_on_expense_delete(sender, instance, **kwargs):
#     def add_balance():
#         account = instance.account
#         amount = Decimal(str(instance.amount)) if not isinstance(
#             instance.amount, Decimal) else instance.amount
#         account.balance += amount
#         account.save()

#     transaction.on_commit(add_balance)

# # --------------------------- Handle Expenses Automatically --------------------------


# @receiver(post_save, sender=Donation)
# def update_account_balance_on_expense(sender, instance, created, **kwargs):
#     def update_balance():
#         account = instance.account
#         amount = Decimal(str(instance.amount)) if not isinstance(
#             instance.amount, Decimal) else instance.amount

#         if created:
#             account.balance -= amount
#             account.save()

#     transaction.on_commit(update_balance)


# @receiver(post_delete, sender=Donation)
# def add_account_balance_on_expense_delete(sender, instance, **kwargs):
#     def add_balance():
#         account = instance.account
#         amount = Decimal(str(instance.amount)) if not isinstance(
#             instance.amount, Decimal) else instance.amount
#         account.balance += amount
#         account.save()

#     transaction.on_commit(add_balance)
