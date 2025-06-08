from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Income, Expense, CreditCard

from django.contrib.auth import get_user_model
MyUser = get_user_model()


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    model = MyUser

    # list_display = ['username', 'first_name', 'role']
    fieldsets = (
        ('Username & Password', {"fields": ('username', 'password', 'role')}),
        ('Extra Fields', {
            "fields": ('first_name', 'last_name', 'gender', 'contact_no', 'profile_img'),
        }),
        ('permissions', {
            "fields": (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )

    # Fields shown on the first page when adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'role'),
        }),
    )


# admin.site.register(Account)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(CreditCard)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bank', 'balance', 'created_at')