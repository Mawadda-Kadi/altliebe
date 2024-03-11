from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import UserRegisterForm, ProfileForm
from products.models import Product, Wishlist
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Authenticate and login the user
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Account created for {username}! You are now able to log in')
                return redirect('user-profile', username=username)
            else:
                messages.error(request, 'Account creation failed. Please try again.')
        else:
            print(form.errors)  # For debugging
    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        username = self.request.user.username
        return reverse('user-profile', kwargs={'username': username})


# User Profile View
@login_required
def profile_view(request, username):
    # Get the user object for the profile being viewed
    profile_user = get_object_or_404(User, username=username)
    # Compare with the logged-in user
    own_profile = request.user == profile_user

    # Get wishlist for the profile_user
    wishlist_items = Wishlist.objects.filter(user=profile_user)

    context = {
        'profile_user': profile_user,
        'own_profile': own_profile,
        'wishlist_items': wishlist_items,
    }

    return render(request, 'users/profile.html', context)


# Profile Update View
class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_edit.html'

    def get_success_url(self):
        """ Redirect to the user's profile page after successful profile update """
        return reverse_lazy('user-profile', kwargs={'username': self.request.user.username})

    def get_object(self, queryset=None):
        """ Ensure that user can only edit their own profile """
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Your profile was successfully updated.')
        return super().form_valid(form)

# Delete Account View
class AccountDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'users/account_confirm_delete.html'
    # Redirect to product list view after deletion
    success_url = reverse_lazy('product-list')

    def get_object(self, queryset=None):
        """ Ensure the user can only delete their own profile """
        return self.request.user

    def post(self, request, *args, **kwargs):
        """Handle POST request to delete User and related Profile."""
        # This deletes the User
        response = super().post(request, *args, **kwargs)
        # Log the user out
        logout(request)
        messages.success(request, "Your account has been successfully deleted.")
        return response