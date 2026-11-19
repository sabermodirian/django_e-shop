from django.conf import settings
from django.db import models


class Order(models.Model):
    """اطلاعات ثبت سفارش، خریدار و وضعیت پرداخت را نگه می‌دارد."""

    # ارتباط سفارش با کاربری که آن را ثبت کرده است.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # سفارش تا پیش از ثبت پرداخت، پرداخت‌نشده در نظر گرفته می‌شود.
    is_paid = models.BooleanField(default=False)

    # اطلاعات تماس و نشانیِ ثبت‌شده برای این سفارش.
    first_nm = models.CharField(max_length=100)
    last_nm = models.CharField(max_length=100)
    phone_nmbr = models.CharField(max_length=15)
    address = models.CharField(max_length=700)
    order_notes = models.TextField(blank = True)
	   
    # زمان ایجاد سفارش و آخرین ذخیرهٔ آن.
    dttm_created_at = models.DateTimeField(auto_now_add=True)
    dttm_modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return f'Order {self.id}'

class OrderItem(models.Model):
	itms_ordr = models.ForeignKey('orders.Order' , on_delete = models.CASCADE , related_name = 'items_rel_ordr')
	prdct_ordr =  models.ForeignKey('products.Product' , on_delete = models.CASCADE , related_name = 'prdct_rel_ordr')
	qntt_prdct_ordr = models.PositiveIntegerField(default = 1) #quantity of products in order
	price_prdct_ordr = models.PositiveIntegerField()
	
	# زمان ایجادمحصولات قابل  سفارش و آخرین ذخیرهٔ آن.
	prdct_ordr_created_at = models.DateTimeField(auto_now_add = True)
	prdct_ordr_modified_at = models.DateTimeField(auto_now = True)
	
	def __str__(self) :
		return f'OrderItem wit ID: {self.id}: for Pruduct {self.prdct_ordr} X {self.qntt_prdct_ordr} \
	with Pice : {self.price_prdct_ordr}'