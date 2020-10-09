from django.urls import path
from .views import ProductListView, ProductSlugDetailView

urlpatterns = [
    path('', ProductListView, name='list'),
    # path('<int:pk>/', ProductDetailView.as_view()),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
    path('<slug:slug>/', ProductSlugDetailView.as_view(), name='productdetail'),
]
