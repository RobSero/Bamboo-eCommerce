from django.urls import path
from .views import ProductListView, ProductDetailView, ProductFeaturedDetailView, ProductFeaturedListView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
]
