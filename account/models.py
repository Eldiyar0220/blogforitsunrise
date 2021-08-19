from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name =  models.CharField(max_length=150)
    last_name =  models.CharField(max_length=250)


    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.get_full_name()