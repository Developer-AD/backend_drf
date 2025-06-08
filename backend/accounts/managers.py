from django.db import models


# ----------------------------- Custom User Manager ---------------------------------------------
class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# accounts = Account.objects.all() # Filtered objects.
# accounts = Account.all_objects.all() # All objects.
