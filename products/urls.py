from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete


urlpatterns = [
    path('', ProductList.as_view(), name='product-list'),
    path('create/', ProductCreate.as_view(), name='product-create'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('<slug:slug>/update/', ProductUpdate.as_view(), name='product-update'),
    path('<slug:slug>/delete/', ProductDelete.as_view(), name='product-delete'),
    path('profile/<slug:username>/', views.profile_view, name='user-profile'),
]