from django.db import models
from django.db.models.signals import pre_save, post_save
from carts.models import Cart
import random
import string

CHOOSE_ORDER_STATUS = [
  ('created', 'Created'),
  ('paid', 'Paid'),
  ('shipped', 'Shipped'),
  ('refunded', 'Refunded')
]


class Order(models.Model):
  order_id = models.CharField(max_length=20, blank=True)
  # billing_profile = 
  # shipping_address = 
  # billing_address = 
  cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
  status = models.CharField(max_length=100, default='created', choices=CHOOSE_ORDER_STATUS)
  shipping_total = models.DecimalField(default=3.99, max_digits=10, decimal_places=2)
  total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.order_id
  
  
  
  
  
  
def pre_save_order_id_generator(sender,instance, *args, **kwargs):
  if not instance.order_id:
    instance.order_id = ''.join(random.choices(string.ascii_uppercase + string.digits,k=20))

pre_save.connect(pre_save_order_id_generator,sender=Order)