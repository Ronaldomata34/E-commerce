from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from .models import Product

class ProductList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/games.html'

class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_products'] = Product.objects.all()
        return context

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/detail_game.html'