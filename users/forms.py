from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, State, City

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Select State")
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select City")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'state', 'city']

    def clean_password2(self):
        """ Custom validation to check that the two password entries match """
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        profile, created = Profile.objects.update_or_create(
            user=user,
        )
        return user

class ProfileForm(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Select State")
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select City")
    
    class Meta:
        model = Profile
        # Editable fields
        fields = ['about_me', 'state', 'city' ]
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }
