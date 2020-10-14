from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, re_path
from pages.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('search/', include('search.urls')),
    path('cart/', include('carts.urls')),
    path('account/', include('accounts.urls')),
    path('watchlist/', include('watchlist.urls')),
    path('', include('pages.urls')),
    re_path(r'^.*$', home_page)
]

