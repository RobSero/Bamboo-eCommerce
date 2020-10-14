from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# Create your models here.
class Address(models.Model):
  address_name = models.CharField(max_length=25)
  address_one = models.CharField(max_length=200)
  address_two = models.CharField(max_length=200, blank=True, null=True)
  county = models.CharField(max_length=50)
  postcode = models.CharField(max_length=8)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  

  