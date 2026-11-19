from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order , OrderItem  # == from Orders.models import Order , OrderItem


# Create your TabularInLine here :
class OrderItemInline(admin.TabularInline) :  # class OrderItemInline(admin.ُStackedInline):
	"""قراره که کانتهای هر محصول زیر همون Product  در پنل ادمین قابل دسترسی و نمایش باشه """
	model = OrderItem
	fields = ["itms_ordr" , "price_prdct_ordr" , "prdct_ordr" , "qntt_prdct_ordr"]
	extra = 2


# Register your models here.
@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin , admin.ModelAdmin) :
	model = Order
	list_display = ('user'  , 'first_nm' , 'last_nm' , 'dttm_created_at' , 'is_paid')
	
	inlines = [
		OrderItemInline ,
		# باید به Order هم بفهمانیم که OrderItem قرار است در زیرمجموعه ی هر سفارش محصول قابل دسترسی هم باشند
	]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin) :
	model = OrderItem
	list_display = [
		"itms_ordr" , "price_prdct_ordr" , "prdct_ordr" , "qntt_prdct_ordr" ,
	]

# Register your models here.
