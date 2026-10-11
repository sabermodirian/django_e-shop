from django.views import generic


from products.models import Product
# Create your views here.

class ProductListView(generic.ListView):
	model = Product
	template_name = 'products/products_list.html'
	context_object_name = 'products'
	

