import uuid
from django.db import models
from django.contrib.auth import get_user_model

MyUser = get_user_model()


# --------------------------------- Base Model----------------------------------------------
class BaseModel(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    # objects = CustomManager()
    # all_objects = models.Manager()

    class Meta:
        abstract = True
        # ordering = ['-id']

# --------------------------------- Account Model----------------------------------------------


class Account(BaseModel):
    BANK_CHOICES = (
        ('SBI', 'SBI'),
        ('HDFC', 'HDFC'),
        ('Cash', 'Cash'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    bank = models.CharField(max_length=50, choices=BANK_CHOICES, default='Other')
    account_number = models.CharField(max_length=30, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.bank} ({self.account_number})"

# --------------------------------- Income Model----------------------------------------------


class Income(BaseModel):
    SOURCES = (
        ('Salary', 'Salary'),
        ('Return Money', 'Return Money'),
        ('Commission', 'Commission'),
        ('Gift', 'Gift'),
        ('Loan', 'Loan'),
        ('Other', 'Other'),
    )

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='incomes')
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    source = models.CharField(
        max_length=100, choices=SOURCES, default='Other', null=True, blank=True)
    date_received = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.amount} from {self.source}"

# --------------------------------- Expense Model----------------------------------------------


class Expense(BaseModel):
    CATEGORIES = (
        ('Send Money', 'Send Money'),
        ('Rent', 'Rent'),
        ('Gift', 'Gift'),
        ('Food', 'Food'),
        ('Groceries', 'Groceries'),
        ('Transport', 'Transport'),
        ('Bills', 'Bills'),
        ('Shopping', 'Shopping'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    )

    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='expenses')
    category = models.CharField(
        max_length=100, choices=CATEGORIES, default='Other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_spent = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Expense {self.id}: {self.amount} on {self.category}"

# --------------------------------- Donation Model----------------------------------------------


class Donation(BaseModel):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Donation {self.id}: {self.amount} of {self.amount}"


class CreditCard(BaseModel):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')
    name = models.CharField(max_length=100, null=True, blank=True)
    card_number = models.CharField(max_length=20, null=True, blank=True)
    bill_generation_date = models.DateField(null=True, blank=True)
    bill_due_date = models.DateField(null=True, blank=True)
    bill_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    available_limit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    total_limit = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    is_paid = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.id}-{self.name}-{self.card_number}"

    class Meta:
        ordering = ['-bill_generation_date']


class BillPayment(BaseModel):
    BILL_TYPES = (
        ('Mobile Recharge', 'Mobile Recharge'),
        ('Electricity', 'Electricity'),
        ('Loan EMI', 'Loan EMI'),
        # ('Internet Bill', 'Internet Bill'),
        # ('Insurance Premium', 'Insurance Premium'),
        ('Other', 'Other'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    )

    bill_type = models.CharField(
        max_length=50, choices=BILL_TYPES, default='Other')
    account_number = models.CharField(max_length=50, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    class Meta:
        ordering = ['-due_date']


# class Payment(models.Model):
#     credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='payments')
#     payment_date = models.DateField(auto_now_add=True)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)

# Get all unpaid bills
# unpaid_bills = CreditCard.objects.filter(is_paid=False)

# # Get bills due in the next 7 days
# today = date.today()
# next_week = today + timedelta(days=7)
# upcoming_bills = CreditCard.objects.filter(bill_due_date__range=[today, next_week])
