from django.urls import path
from .models import Profile
from .views import register, CustomLoginView, profile_view, ProfileUpdate, AccountDelete
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/edit/', ProfileUpdate.as_view(), name='edit-profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/<str:username>/', profile_view, name='user-profile'),
    path('delete-account/', AccountDelete.as_view(), name='delete-account'),
]

