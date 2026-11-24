from django.urls import path

from .views import add_to_cart_view , cart_detail_view , clear_cart , remove_from_cart_view , update_cart_view


app_name = 'cart'

urlpatterns = [
	path('' , cart_detail_view , name = 'cart_detail' ) ,
	# برای فرستادن پروداکت مورد نظر از پروداکت دیتیل ویو به داخل کارت ویو
	path('add/<int:product_id>/' , add_to_cart_view , name = 'adding_to_cart') ,
	
	# برای کلیک روی Refresh  و  تغییر تعداد محصول و بازگشت به cart_detail
	path('update/<int:product_id>/' , update_cart_view , name = 'update_cart') ,
	
	# برای حذف یک پروداکت مورد نظر از سبد خرید بازدن دکمه ی ضربدرقرمز
	path('remove/<int:product_id>/' , remove_from_cart_view , name = 'remove_from_cart') ,
	# برای خالی کردن کل پروداکتهای   سبد خرید بازدن دکمه ی خالی کردن سبد خرید
	path('clear/' , clear_cart , name = 'clear_cart') ,

]
