from django.shortcuts import get_object_or_404 , redirect , render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils .translation import gettext_lazy as _

from products.models import Product

from .cart import Cart
from .forms import AddToCartProductForm


# Create your views here.

def cart_detail_view(request):
	cart = Cart(request)
	
	for item in cart:
		item['prdct_update_quntt_form'] = AddToCartProductForm(initial ={
			'quantity': item['quantity'],
			'inplace':True,
		} ) #initial: برای همه ی فرمها وجود دارد بطور پیشفرض
		
	
	return render(request, 'cart/cart_detail.html', {
		'cart': cart,
	})

@require_POST # این ویو فقط حق دارد بصورت POST Request صدا زده شود
def add_to_cart_view(request, product_id):
    cart_obj = Cart(request)

    prdct_obj = get_object_or_404(
        Product,
        id=product_id
    )

    cart_form = AddToCartProductForm(request.POST)

    if cart_form.is_valid():
        cleaned_data = cart_form.cleaned_data
        qntty = cleaned_data['quantity']

        cart_obj.add_prdct(
            prdct_obj,
            qntty,
            replace_current_quntt=cleaned_data['inplace'],
            show_message = False ,
        )
        
        # پیام فقط اینجا ساخته می‌شود؛ بنابراین هنگام افزودن محصول
        # فقط یک پیام موفقیت نمایش داده خواهد شد.
        messages.success(
	        request ,
	        _('Your product was added to the cart successfully!')
        )
    
    else :
	    messages.error(
		    request ,
		    _('The product information is not valid.')
	    )
	    
	    # بعد از اضافه‌کردن محصول، کاربر به لیست محصولات برمی‌گردد.
    return redirect('product_list')


@require_POST
# این ویو فقط برای Refresh یا به‌روزرسانی تعداد محصول در سبد است.
def update_cart_view(request, product_id):
    cart_obj = Cart(request)
    prdct_obj = get_object_or_404( Product,id=product_id)
    cart_form = AddToCartProductForm(request.POST)

    if request.method == 'POST' and cart_form.is_valid():
        cleaned_data = cart_form.cleaned_data
        qntty = cleaned_data['quantity']
        
        cart_obj.add_prdct(prdct_obj,qntty,
                           replace_current_quntt=True,
                           show_message=False,
							)
        # پیام Refresh فقط در همین ویو ساخته می‌شود.
        messages.success(
	        request ,
	        _('Product quantity was updated successfully!')
        )
    
    else :
	    messages.error(
		    request ,
		    _('The quantity entered is not valid.')
	    )
	    
	    # بعد از Refresh، کاربر در همان صفحه سبد خرید باقی می‌ماند.
    return redirect('cart:cart_detail')

"""
replace_current_qntt=True  :نکتهٔ مهم اینجاست
چون در Refresh می‌خواهیم مقدار قبلی جایگزین شود،
 نه اینکه دوباره به مقدار قبلی اضافه شود. اگر این مقدار را False بگذاری،
  کاربر مثلاً عدد ۳ وارد می‌کند و سبد ممکن است دوباره ۳ تا روی مقدار قبلی اضافه کند؛
   سبد خرید هم تبدیل می‌شود به ماشین تولید محصول، کاملاً بی‌خبر از اقتصاد خانواده! 😄
"""


def remove_from_cart_view(request, product_id):
	cart_obj = Cart(request)
	
	prdct_obj = get_object_or_404(Product , id = product_id)
	cart_obj.remove_prdct(prdct_obj)
	return redirect('cart:cart_detail')

@require_POST
def clear_cart(request):
	cart_obj = Cart(request)
	
	if  len(cart_obj) != 0:
		cart_obj.clear_cart()
		messages.success(
			request ,
			_('All products erased successfully from your Cart!')
		)
	else :
		messages.warning(
			request ,
			_('Your Cart is already empty!')
		)
	
	# پیام خالی‌کردن سبد در صفحه خود سبد نمایش داده می‌شود.
	return redirect('cart:cart_detail')

	
	
	
	