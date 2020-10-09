from django.urls import path, include
from .views import watchlist, update_watchlist

urlpatterns = [
    path('', watchlist, name='watching'),
    path('<int:product_id>', update_watchlist, name='watchlist')
]