from django import forms
from .models import Product, ProductImage

# Choices Fields
CATEGORY = (
    (0, "Electronics"),
    (1, "Fashion and Apparel"),
    (2, "Home and Garden"),
    (3, "Sports and Outdoors"),
    (4, "Toys and Games"),
    (5, "Books and Media"),
    (6, "Pet Supplies"),
    (7, "Others")
)
STATUS = (
    (0, "used"), (1, "new"), (2, "handmade")
)

class ProductSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'featured_image', 'description', 'category', 'price', 'status', 'availability']


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']