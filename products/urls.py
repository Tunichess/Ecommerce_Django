from django.urls import path
from products.views  import (
    ProductListView, 
    # product_list_view,
    ProductDetailView,
    ProductDetailSlugView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    # AccessoresListView,
    )

app_name='products'

urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    # path('accessores',AccessoresListView.as_view(), name='accessores'),

    # path('featured',ProductFeaturedListView.as_view()),
    path('<int:pk>/', ProductDetailView.as_view()),
    path('<slug>/', ProductDetailSlugView.as_view(), name='detail'),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
]