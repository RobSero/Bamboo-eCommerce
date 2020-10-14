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
  # shipping_address = 
  # billing_address = 
  cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
  status = models.CharField(max_length=100, default='created', choices=CHOOSE_ORDER_STATUS)
  shipping_total = models.DecimalField(default=3.99, max_digits=10, decimal_places=2)
  total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
  
  def __str__(self):
    return self.order_id
  
  def update_total(self):
    self.total = round(float(self.cart.total) + float(self.shipping_total),2)
    self.save()
    return self.total
  
  
  
  # PRIOR TO ORDER BEING SAVED, A RANDOM ID IS GENERATED FOR IT - ONLY RUNS WHEN ORDER IS CRATED AND HAS NO ID
def pre_save_order_id_generator(sender,instance, *args, **kwargs):
  if not instance.order_id:
    instance.order_id = ''.join(random.choices(string.ascii_uppercase + string.digits,k=20))

pre_save.connect(pre_save_order_id_generator,sender=Order)

# FIRES WHEN CART IS SAVED, WILL UPDATE TOTAL OF ORDER
def post_save_cart_update_order(sender,instance, created, *args, **kwargs):
  if not created:
    cart = instance
    find_order = Order.objects.filter(cart__id=cart.id)
    if find_order.count() == 1:
      order = find_order.first()
      order.update_total()

post_save.connect(post_save_cart_update_order, sender=Cart)


# FIRES WHEN AN ORDER IS INITIALLY CREATED, WILL CALCULATE THE TOTAL BASED ON THE CART IT IS ASSIGNED TO
def post_save_order(sender,instance, created, *args, **kwargs):
  if created:
    print('CART CREATED - UPDATING TOTAL')
    instance.update_total()
    
post_save.connect(post_save_order, sender=Order)