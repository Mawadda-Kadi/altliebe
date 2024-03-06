from .forms import ProductSearchForm

def product_search_form(request):
    return {'product_search_form': ProductSearchForm()}