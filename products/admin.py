from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Product    # == from Product.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('title', 'datetime_created', 'datetime_modified' , 'price' , 'active' ,)