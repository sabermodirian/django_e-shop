from django.urls import path

from .views import add_to_cart_view , cart_detail_view

app_name = 'cart'

urlpatterns = [
	path('', cart_detail_view , name = 'cart_detail' ,),
	path('add/<int:product_id>/' , add_to_cart_view, name = 'adding_to_cart'),
	# برای فرستادن پروداکت مورد نظر از پروداکت دیتیل ویو به داخل کارت ویو
]