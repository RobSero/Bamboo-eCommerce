from django.urls import path, include
from .views import update_watchlist

urlpatterns = [
    path('<int:product_id>', update_watchlist, name='watchlist')
]