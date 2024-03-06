from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, State, City
from .forms import UserRegisterForm, ProfileForm
from products.models import Product
import logging


# Get an instance of a logger
logger = logging.getLogger(__name__)


# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This returns the User object after saving

            # Authenticate and login the user automatically after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Account created for {username}! You are now able to log in')
                return redirect('user-profile', username=username)
        else:
            # If the form is invalid, render the form again with error messages
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        username = self.request.user.username
        return reverse('user-profile', kwargs={'username': username})

# User Profile View
@login_required
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    own_profile = request.user == user
    return render(request, 'users/profile.html', {'profile': user.profile, 'own_profile': own_profile})

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
class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'users/profile_confirm_delete.html'
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