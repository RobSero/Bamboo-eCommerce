from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class Watchlist(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  products = models.ManyToManyField(Product)
  
  def __str__(self):
    return self.user.email
  

def create_watchlist(sender,instance, created, *args, **kwargs):
  if created:
    new_watchlist = Watchlist.objects.create(user=instance)
    

post_save.connect(create_watchlist, sender=User)