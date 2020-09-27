from django.urls import path
from .views import home_page, about_page, contact_page, login_page

urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('login/', login_page)
]
