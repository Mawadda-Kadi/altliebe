from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm


""" Test Register """
class RegisterTestCase(TestCase):
    def test_register_success(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }

        response = self.client.post(url, data)
        # Redirect status code
        self.assertEqual(response.status_code, 302)

        # Check that the user was created
        user_model = get_user_model()
        self.assertTrue(user_model.objects.filter(username='testuser').exists())

        # Check that the user is authenticated and redirect them to profile page
        self.assertRedirects(response, reverse('user-profile', kwargs={'username': 'testuser'}))

    def test_register_failure(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'abcdef123456',
            'password2': 'wrongpassword'
        }

        response = self.client.post(url, data)
         # Return to the same page on error
        self.assertEqual(response.status_code, 200)

        # Check that the user was not created
        user_model = get_user_model()
        self.assertFalse(user_model.objects.filter(username='testuser').exists())


""" Test User Profile """
class UserProfileViewTest(TestCase):
    def setUp(self):
        # Create a test user for login
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_view_own_profile(self):
        # Test viewing the logged-in user's own profile
        response = self.client.get(reverse('user-profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('own_profile' in response.context)
        self.assertTrue(response.context['own_profile'])

    def test_view_other_profile(self):
        # Create another user to test viewing another user's profile
        other_user = User.objects.create_user(username='otheruser', password='12345')
        response = self.client.get(reverse('user-profile', kwargs={'username': other_user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['own_profile'])

    def test_profile_not_found(self):
        # Test viewing a profile that does not exist
        response = self.client.get(reverse('user-profile', kwargs={'username': 'nonexistent'}))
        self.assertEqual(response.status_code, 404)
