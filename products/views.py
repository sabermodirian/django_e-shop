from django.views import generic

from products.forms import CommentForm
from products.models import Comment , Product
# Create your views here.

class ProductListView(generic.ListView):
	# model = Product
	queryset = Product.objects.filter(active = True)
	template_name = 'products/products_list.html'
	context_object_name = 'products'
	
class ProductDetailsView(generic.DetailView):
	model = Product
	template_name = 'products/product_details.html'
	context_object_name = 'product'
	
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['comment_form'] = CommentForm()
	# 	return context
	
	def get_context_data(self , **kwargs) :
		"""
		ساخت و تکمیل داده‌های قابل ارسال به قالب جزئیات محصول.

		This method builds and extends the context data sent to the
		product details template.

		Returns:
			dict: دیکشنری شامل اطلاعات محصول و فرم ثبت نظر.
				  A dictionary containing the product data and comment form.
		"""
		
		# دریافت context پیش‌فرض از کلاس والد DetailView
		# Get the default context data from the parent DetailView class.
		context = super().get_context_data(**kwargs)
		
		# ایجاد فرم خالی ثبت نظر و اضافه‌کردن آن به context
		# Create an empty comment form and add it to the context.
		context["comment_form"] = CommentForm()
		
		# برگرداندن context تکمیل‌شده به قالب
		# Return the extended context to the template.
		return context

class CommentCreateView(generic.CreateView):
	model = Comment
	form_class = CommentForm
	
	def form_valid(self, form):
		obj_frm_cmmnt_mdl = form.save(commit = False)
		obj_frm_cmmnt_mdl.author_cmmnt = self.request.user
		return super().form_valid(form)
	 
	
