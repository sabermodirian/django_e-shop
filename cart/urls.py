from django.urls import path

from .views import add_to_cart_view , cart_detail_view , remove_from_cart_view

app_name = 'cart'

urlpatterns = [
	path('', cart_detail_view , name = 'cart_detail' ,),
# برای فرستادن پروداکت مورد نظر از پروداکت دیتیل ویو به داخل کارت ویو
	path('add/<int:product_id>/' , add_to_cart_view, name = 'adding_to_cart'),
	
	# برای حذف یم پروداکت مورد نظر از سبد خرید بازدن دکمه ی ضربدرقرمز
path('remove/<int:product_id>/' , remove_from_cart_view, name = 'remove_from_cart'),
]