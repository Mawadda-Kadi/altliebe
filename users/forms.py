from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, State, City

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    state = forms.ModelChoiceField(queryset=State.objects.all())
    # Initially, this will be empty
    city = forms.ChoiceField(choices=[('', '---------')], required=False)
    #state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Select State")
    #city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select City")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'state', 'city']

    def clean_password2(self):
        """ Custom validation to check that the two password entries match """
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean(self):
        cleaned_data = super().clean()
        state_id = cleaned_data.get('state')
        city_name = cleaned_data.get('city')
        # Dynamically adjust the city queryset based on the state
        if state_id:
            self.fields['city'].queryset = City.objects.filter(state_id=state_id)
            # Validate the city choice against the new queryset
            if city_name and not self.fields['city'].queryset.filter(name=city_name).exists():
                self.add_error('city', 'Select a valid choice. That city is not one of the available choices.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            city_name = self.cleaned_data.get('city')
            state = self.cleaned_data.get('state')
            print(f"Saving user: {user.username}, State: {state}, City: {city_name}")  # Debug print
            city, created = City.objects.get_or_create(name=city_name, state=state)
            print(f"City: {city}, Created: {created}")  # Debug print
            profile, profile_created = Profile.objects.update_or_create(
                user=user,
                defaults={'city': city},
            )
            print(f"Profile updated or created: {profile_created}")  # Debug print
            return user

class ProfileForm(forms.ModelForm):
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, empty_label="Select State")
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, empty_label="Select City")

    class Meta:
        model = Profile
        # Editable fields
        fields = ['featured_image', 'about_me', 'state', 'city' ]
        widgets = {
            'about_me': forms.Textarea(attrs={'rows': 4}),
        }
