from django.db import models
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.name}'

class User(AbstractUser):
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    #profile_image = models.ImageField()
    email = models.EmailField(null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    about = models.TextField(null=True,blank=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
