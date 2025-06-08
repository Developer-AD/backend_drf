from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


# Create your models here.


# --------------------------------- Custom User Model----------------------------------------------
class MyUser(AbstractUser):
    """User model."""

    USER_CHOICES = (
        (1, 'User'),
        (2, 'Admin'),
    )

    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )
    # Use UUID only for Production else you will find difficulty while api testing to pass the id.
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.IntegerField(choices=USER_CHOICES, blank=True, null=True, default=1)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    contact_no = models.CharField(max_length=30, blank=True, null=True)
    profile_img = models.ImageField(upload_to='profiles/', blank=True, null=True)

    # email = models.EmailField(max_length=50, unique=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['id']