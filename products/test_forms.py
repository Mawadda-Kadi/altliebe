from django.test import TestCase
from .forms import ProductSearchForm

class ProductSearchFormTest(TestCase):

    def test_form_empty(self):
        # Test the form with no data
        form = ProductSearchForm({})
        # The form should be valid even if empty
        self.assertTrue(form.is_valid())

    def test_form_with_query(self):
        # Test the form with a search query
        form = ProductSearchForm({'query': 'test'})
        # The form should be valid with data
        self.assertTrue(form.is_valid())

        # Check if the query data is correctly handled
        self.assertEqual(form.cleaned_data['query'], 'test')

    def test_form_with_whitespace_query(self):
        # Test the form with a query that contains only whitespace
        form = ProductSearchForm({'query': '   '})
        # The form should still be valid
        self.assertTrue(form.is_valid())

        # Check if the query is stripped
        self.assertEqual(form.cleaned_data['query'], '')