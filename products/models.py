from django.db import models
import random
import os


def upload_image_path(instance, filename):
  new_filename = random.randint(1,200000)
  base_name = os.path.basename(filename)
  name, ext = os.path.splitext(base_name)
  final_filename = f'products/{new_filename}/{new_filename}{ext}'
  return final_filename


# #  --- CREATE METHODS TO BE USED ON THE get_queryset METHOD
# class ProductQuerySet(models.query.QuerySet):
#   def featured(self):  # creates the method: get_queryset().featured()
#     return self.filter(featured=True)
  
#   def active(self):  # creates the method: get_queryset().active()
#     return self.filter(active=True)


# --- CREATES METHODS THAT CAN BE USED ON THE Product.objects METHOD
class ProductManager(models.Manager):
  def get_by_id(self, id):
    return self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
  
  def active(self):
    return self.get_queryset().filter(active=True)
  
  def feature(self):  # allows for the use of Product.objects.feature()
    return self.get_queryset().filter(featured=True)



class Product(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(default='abc')
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=10, default=0.99)
  image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  featured = models.BooleanField(default=False)
  active = models.BooleanField(default=True)
  
  objects = ProductManager()
  
  def __str__(self):
    return f'{self.title} - Product'


