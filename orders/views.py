from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItem


# Create your views here.

@login_required
def order_create_view(request):
	"""فرم سفارش را نمایش می‌دهد و سفارش معتبر را برای کاربر ذخیره می‌کند."""
	order_frm = OrderForm()
	cart_obj = Cart(request)
	
	if request.method == 'POST':
		order_frm = OrderForm(request.POST,)
		
		if order_frm.is_valid(): # در این خط اگر به ارور بخوریم در خودش(order_frm) ذخیره میکند
			order_obj = order_frm.save(commit = False)# و دگر وارد این بلاک نمیشود
			# commit=False شیء سفارش را می‌سازد، اما هنوز در دیتابیس ذخیره نمی‌کند.
			order_obj.user = request.user
			order_obj.save()
			
			for itm_crt_obj in cart_obj:
				prdct_itm = itm_crt_obj["prdct_yld_obj"] # دقیقا همون productی است که در همون لحظه(در لحظه ی زمانی) در  دیتابیس هستش
				OrderItem.objects.create(
					itms_ordr = order_obj, # شیء سفارش
					prdct_ordr = prdct_itm, # itm_crt_obj[prdct_yld_obj] # دقیقا همون productی است که در همون لحظه(در لحظه ی زمانی) در  دیتابیس هستش
					qntt_prdct_ordr = itm_crt_obj['quantity'],
					price_prdct_ordr = prdct_itm.price,
				)
			cart_obj.clear_cart()
			
			# پس از ثبت موفق، از ارسال دوبارهٔ فرم هنگام Refresh جلوگیری می‌کند.
			return redirect(request.path)
	else :
		order_frm = OrderForm()
		
	return render(request,
              'orders/order_create.html',
              {'frm_ordr':order_frm }) # پس order_frm را همراه ارورهایش هم به تمپلیت میفرستیم
													#    و در آنطرف (تمپلیت order_create.htm) با کمک یک حلقه روی ارورهای این  frm_ordr حرکت کرده و همهی ارورها را دریافت و میبینیم و هندل مینیماییم