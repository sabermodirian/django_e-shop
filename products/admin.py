from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Product , Comment   # == from Product.models import Product , Comment


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('title', 'datetime_created', 'datetime_modified' , 'price' , 'active' ,)
	
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = [
		"product_cmmnt", "status_cmmnt", "stars_point_prdct", "cmmnt_body_txt", "author_cmmnt"
	]
 