from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Wishlist
from .forms import ProductForm, ProductSearchForm
from users.models import Profile
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

    def get_queryset(self):
        # Start with all available or reserved products
        queryset = Product.objects.filter(Q(availability=0) | Q(availability=1))
        query = self.request.GET.get('query', '')
        category = self.request.GET.get('category', '')
        seller = self.request.GET.get('seller', '')
        state = self.request.GET.get('state', '')
        status = self.request.GET.get('status', '')

        # Apply search filters
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(seller__username__icontains=query) |
                Q(city__icontains=query)
            )
        if category and category != '':
            queryset = queryset.filter(category=category)
        if status and status != '':
            queryset = queryset.filter(status=status)
        if state:
            queryset = queryset.filter(state=state)

        # Sorting logic
        sort = self.request.GET.get('sort', 'date_desc')
        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')
        elif sort == 'date_asc':
            queryset = queryset.order_by('created_at')
        elif sort == 'date_desc':
            queryset = queryset.order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the search form to the template
        context['form'] = ProductSearchForm(self.request.GET or None)
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_queryset(self):
        """Ensure only available products can be viewed."""
        return super().get_queryset().all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the products
        context['product'] = self.get_object()
        return context


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
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
        form.instance.address = user_profile.state
        return super(ProductCreate, self).form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    fields = ['title', 'featured_image', 'category', 'description', 'price', 'status', 'availability']
    template_name = 'products/product_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    # Redirect to product list view after updte
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        user_profile = self.request.user.profile
        form.instance.city = user_profile.city
        form.instance.address = user_profile.state
        return super().form_valid(form)


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    # Redirect to product list view after deletion
    success_url = reverse_lazy('product-list')


class AddToWishlistView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        # Check if the product is owned by the user
        if product.seller == request.user:
            messages.error(request, "You cannot add your own product to the wishlist.")
            return HttpResponseRedirect(reverse('product-detail', kwargs={'slug': product.slug}))

        # Proceed to add to wishlist if it's not the user's own product
        Wishlist.objects.get_or_create(user=request.user, product=product)
        messages.success(request, "Product added to your wishlist.")
        return HttpResponseRedirect(reverse('product-detail', kwargs={'slug': product.slug}))


@login_required
def wishlist_view(request):
    # Get the wishlist items for the current user
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')

    return render(request, 'products/wishlist.html', {'wishlist_items': wishlist_items})


class RemoveFromWishlistView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        # Get the product and remove it from the user's wishlist
        product = get_object_or_404(Product, id=product_id)
        Wishlist.objects.filter(user=request.user, product=product).delete()
        return redirect('wishlist-view')