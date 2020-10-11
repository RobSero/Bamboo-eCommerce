from django.urls import path
from .views import cart_home, cart_update, checkout_home, set_address

urlpatterns = [
    path('', cart_home, name='carthome'),
    path('update/', cart_update, name='cartupdate'),
    path('checkout/', checkout_home, name='checkout'),
    path('address/', set_address, name='setaddress')
]
