from django.db import models

class Product(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=10, default=0.99)
  
  def __str__(self):
    return f'{self.title} - Product'
