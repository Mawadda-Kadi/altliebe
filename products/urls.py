from django.urls import path
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
from users.views import profile_view


urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/add/', ProductCreate.as_view(), name='product-create'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('products/<slug:slug>/edit/', ProductUpdate.as_view(), name='product-update'),
    path('<slug:slug>/delete/', ProductDelete.as_view(), name='product-delete'),
    #path('profile/<slug:username>/', views.profile_view, name='user-profile'),
]