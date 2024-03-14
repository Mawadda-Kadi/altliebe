from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Profile

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        """Custom validation to check that the two password entries match"""
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    # Define form fields for username and password
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        # Initialize request attribute for form
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        # Retrieve cleaned data for username and password fields
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        # Perform authentication if both username and password are provided
        if username and password:
            # Authenticate user
            self.user_cache = authenticate(self.request, username=username, password=password)
            # Check if authentication failed or user account is inactive
            if self.user_cache is None:
                raise forms.ValidationError('Invalid username or password. Please try again.')
            elif not self.user_cache.is_active:
                raise forms.ValidationError('This account is inactive.')
        return self.cleaned_data



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Editable fields
        fields = ['featured_image', 'email', 'about_me', 'state', 'city' ]
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }

