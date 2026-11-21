from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def order_create_view(request):
	context = {'frm_ordr' : OrderForm(), }
	return render(request, 'orders/order_create.html',context)
