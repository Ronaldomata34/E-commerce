from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import get_object_or_404, get_list_or_404
from cart.forms import CartAddProductForm

from .models import Product, Category, Platform

class ProductList(ListView):
    template_name = 'products/games.html'
    context_object_name = 'games'

    def get_queryset(self):
        self.platform_slug = self.kwargs.get('platform_slug', None)
        self.category_slug = self.kwargs.get('category_slug', None)
        self.category = None
        self.platform = None
        return self.products_filters(self.platform_slug, self.category_slug)
    
    def products_filters(self, platform_slug, category_slug):
        products_list = Product.objects.filter(available=True)
        if platform_slug and category_slug:
            self.platform = get_object_or_404(Platform, slug=platform_slug)
            self.category = get_object_or_404(Category, slug=category_slug)
            products_list = products_list.filter(platform=self.platform, category=self.category)
        elif platform_slug:
            self.platform = get_object_or_404(Platform, slug=platform_slug)
            products_list = products_list.filter(platform=self.platform)
        return products_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        context['platform'] = self.platform
        context['platforms'] = Platform.objects.all()
        return context


class HomePage(ListView):
    template_name = 'home/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.order_by('-created')[:5]
        return queryset


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/detail_game.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm
        return context

    