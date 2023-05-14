from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory
from django.views.generic import ListView, DetailView
# Create your views here.

class ProductListView(ListView):
    model = Product
    paginate_by = 45
    context_object_name = 'products'
    template_name = "product_module/list_view.html"
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_module/detail_view.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']

        return context
