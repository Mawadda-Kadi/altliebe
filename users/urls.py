from django.urls import path
from . import views
from .views import profile_view, CustomLoginView, profile_edit_view, delete_account_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/<str:username>/', views.profile_view, name='user-profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/edit/', profile_edit_view, name='edit-profile'),
    path('delete-account/', delete_account_view, name='delete-account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]