from django.http import HttpResponse
from django.shortcuts import get_object_or_404 , render
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from products.forms import CommentForm
from products.models import Comment , Product

# Create your views here.

# def test_msg(request):
# 	messages.success(request , 'This is a succes message.')
# 	messages.error(request , 'This is a error message.')
# 	messages.warning(request , 'This is a warning message.')
# 	messages.info(request , 'This is a information message.')
# 	return render(request , 'products/test_hello.html')

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
	
	# def get_success_url(self) :
	# 	# self.object همان کامنتِ تازه ذخیره‌شده است!
	# 	# از طریق رابطه اش (related_name = 'rel_prdct_cmmnts') به محصول دسترسی داریم
	# 	return reverse('product_details' , kwargs = {'pk' : self.object.product_cmmnt.pk})
	
	def form_valid(self , form , obj_prdct = None):
		obj_frm_cmmnt_mdl = form.save(commit = False)
		obj_frm_cmmnt_mdl.author_cmmnt = self.request.user
		product_id = int(self.kwargs['prdct_id'])
		prdct = get_object_or_404(Product , id=product_id)
		obj_frm_cmmnt_mdl.product_cmmnt = prdct

		return super().form_valid(form)
	 
	
