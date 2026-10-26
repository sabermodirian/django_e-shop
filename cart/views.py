from django.shortcuts import get_object_or_404 , redirect , render

from products.models import Product
from .cart import Cart
from .forms import AddToCartProductForm


# Create your views here.

def cart_detail_view(request):
	cart = Cart(request)
	
	
	return render(request, 'cart/cart_detail.html', {
		'cart': cart,
	})


def add_to_cart_view(request, product_id):
	cart_obj = Cart(request)
	
	prdct_obj = get_object_or_404(Product, id = product_id)
	cart_form = AddToCartProductForm(request.POST)
	if cart_form.is_valid():
		cleaned_data = cart_form.cleaned_data
		qntty = cleaned_data['quantity']
		cart_obj.add_prdct(prdct_obj,qntty)
	return redirect('cart:cart_detail')
	