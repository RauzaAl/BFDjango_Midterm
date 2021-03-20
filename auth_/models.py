from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    ROLE_CHOICES = (
        (1, "superadmin"),
        (2, "guest")
    )
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, null=True)

    class Meta:
        db_table = 'book_users'


class Profile(models.Model):
    GENDER_CHOICES = (
        (1, "male"),
        (2, "female")
    )
    gender = models.PositiveIntegerField(choices=GENDER_CHOICES, null=True)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="profile")

