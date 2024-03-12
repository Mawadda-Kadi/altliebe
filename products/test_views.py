import os
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .models import Product

class ProductCreateViewTest(TestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_product_create_view(self):
        url = reverse('product-create')
        with open('products/static/products/images/test_image.jpg', 'rb') as file:
            image = SimpleUploadedFile(name='test_image.jpg', content=file.read(), content_type='image/jpeg')
            data = {
                'title': 'Test Product',
                'description': 'This is a test product.',
                'price': '9.99',
                'category': 0,
                'status': 1,
                'featured_image': image,
                'availability': 0,
                # Add management form data for the formset
                'images-TOTAL_FORMS': '1',
                'images-INITIAL_FORMS': '0',
                'images-MIN_NUM_FORMS': '0',
                'images-MAX_NUM_FORMS': '5',
            }
            response = self.client.post(url, data, follow=True)

            # Print form errors if not redirecting
            if response.status_code != 302:
                print(response.context['form'].errors)
            if 'formset' in response.context:
                print(response.context['formset'].errors)
            if response.status_code != 302:
                print(response.content)

            # Check if the product was created and the page redirects to product list
            self.assertRedirects(response, reverse('product-list'), status_code=302, target_status_code=200)
            self.assertEqual(Product.objects.count(), 1)


            # Check the details of the created product
            product = Product.objects.first()
            self.assertEqual(product.title, 'Test Product')
            self.assertEqual(product.seller, self.user)