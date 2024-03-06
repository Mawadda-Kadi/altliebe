from django import forms
from .models import Product
from users.models import State

# Choices Fields
CATEGORY = (
    ('', "Any"),
    (0, "Electronics"),
    (1, "Fashion and Apparel"),
    (2, "Home and Garden"),
    (3, "Sports and Outdoors"),
    (4, "Toys and Games"),
    (5, "Books and Media"),
    (6, "Pet Supplies"),
    (7, "Other")
)
STATUS = (
    ('', "Any"), (0, "used"), (1, "new"), (2, "handmade")
)

class ProductSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    category = forms.ChoiceField(choices=CATEGORY, required=False, label='Category')
    status = forms.ChoiceField(choices=STATUS, required=False)
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Any State", label='State')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'status', 'availability']