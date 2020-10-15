from django.urls import path
from .views import payment_page, charge_card

urlpatterns = [
    path('', payment_page, name='payment'),
    path('charge/', charge_card , name='charge')
]
