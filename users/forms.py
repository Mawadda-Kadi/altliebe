from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # Editable fields
        fields = ['featured_image', 'about_me', 'state', 'city' ]
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }
