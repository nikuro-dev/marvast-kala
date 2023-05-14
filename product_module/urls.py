from django.urls import path,re_path
from .views import ProductListView, ProductDetailView
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    re_path(r'detail/(?P<slug>[-\w]+)/', ProductDetailView.as_view(), name= "product_detail")
]


