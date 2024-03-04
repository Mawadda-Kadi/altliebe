from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, State

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    state = forms.ModelChoiceField(queryset=State.objects.all())
    # Initially, this will be empty
    city = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Editable fields
        fields = ['about_me', 'address', 'city']
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }
