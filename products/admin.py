from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Product , Comment   # == from Product.models import Product , Comment


# Create your TabularInLine here :
class CommentsInlineProduct(admin.TabularInline): # class CommentsInlineProduct(admin.ُStackedInline):
	"""قراره که کانتهای هر محصول زیر همون Product  در پنل ادمین قابل دسترسی و نمایش باشه """
	model = Comment
	fields = ["status_cmmnt", "stars_point_prdct", "cmmnt_body_txt", "author_cmmnt"]
	extra = 5
	
	
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	model = Product
	list_display = ('title', 'datetime_created', 'datetime_modified' , 'price' , 'active' ,)
	
	inlines = [
		CommentsInlineProduct, #  باید به Product هم بفهمانیم که کامنتها قرار است در زیرمجموعه ی هر محصول قابل دسترسی هم باشند
	]
	
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = [
		"product_cmmnt", "status_cmmnt", "stars_point_prdct", "cmmnt_body_txt", "author_cmmnt"
	]
 