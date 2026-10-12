from django.views import generic


from products.models import Product
# Create your views here.

class ProductListView(generic.ListView):
	# model = Product
	queryset = Product.objects.filter(active = True)
	template_name = 'products/products_list.html'
	context_object_name = 'product'
	
class ProductDetailsView(generic.DetailView):
	model = Product
	template_name = 'products/product_details.html'
	context_object_name = 'product'
	

