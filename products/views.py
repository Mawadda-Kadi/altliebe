from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm
import logging

User = get_user_model()
logger = logging.getLogger(__name__)

def my_function():
    logger.debug('This is a debug message')

# Create your views here.

class ProductList(generic.ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = 'products'
    paginate_by = 4

    def product_list(request):
        products = Product.objects.filter(Q(availability=0) | Q(availability=1))
        return render(request, 'products/product_list.html', {'products': products})

    def get_queryset(self):
        """Override to customize the query."""
        return Product.objects.all().order_by('-created_at')


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_queryset(self):
        """Ensure only available products can be viewed."""
        return super().get_queryset().all()

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    # Redirect to product list view after creation
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = None
        return context

    def form_valid(self, form):
        form.instance.seller = self.request.user
        user_profile = self.request.user.profile
        form.instance.city = user_profile.city
        form.instance.city.state = user_profile.city.state
        return super(ProductCreate, self).form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'description', 'price', 'status', 'availability']
    template_name = 'products/product_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # Redirect to product list view after updte
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        user_profile = self.request.user.profile
        form.instance.city = user_profile.city
        form.instance.address = user_profile.address
        return super().form_valid(form)

class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    # Redirect to product list view after deletion
    success_url = reverse_lazy('product-list')
