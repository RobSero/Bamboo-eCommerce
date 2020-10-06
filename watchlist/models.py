from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

# Create your models here.
class Watchlist(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  products = models.ManyToManyField(Product)
  
  def __str__(self):
    return self.user.email