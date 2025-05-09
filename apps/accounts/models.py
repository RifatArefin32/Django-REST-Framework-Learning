from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male')
    
    def save(self, *args, **kwargs):
        if not self.id:
            last_user = CustomUser.objects.order_by('-id').first()
            self.id = (last_user.id + 1) if last_user and last_user.id else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username