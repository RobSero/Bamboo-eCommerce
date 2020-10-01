from django.db import models
from django.conf import settings
from products.models import Product

User = settings.AUTH_USER_MODEL

# Create your models here.
class Cart(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
  products = models.ManyToManyField(Product, blank=True)
  total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  # def __str__(self):
  #   return (self.id)