from django.db import models
from products.models import Product

# Create your models here.
class Tag(models.Model):
  title = models.CharField(max_length=20)
  slug = models.SlugField(default=title)
  timestamp = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)
  products = models.ManyToManyField(Product, blank=True)
  
  def __str__(self):
    return self.title