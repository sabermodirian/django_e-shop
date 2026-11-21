from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
# Create your views here.

@login_required
def order_create_view(request):
	if request.method == 'POST':
		order_frm = OrderForm(request.POST,)
		if order_frm.is_valid():
			order_frm.save(commit = False)
			order_obj.user = request.user
			order_obj.save()
	
	
	# context = {'frm_ordr' : OrderForm(), }
	return render(request, 'orders/order_create.html')
