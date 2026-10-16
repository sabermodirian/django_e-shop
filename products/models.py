
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length = 100 , verbose_name = _("Product's Name"))
	description = models.TextField(verbose_name = _("Product's Features"))
	price = models.PositiveIntegerField(default = 0 , verbose_name = _("Price"))
	active = models.BooleanField(default = True, verbose_name = _("confirmed Product"))
	
	# cover_prdct = models.ImageField()
	datetime_created = models.DateTimeField(auto_now_add = True, verbose_name = _("Product Created At"))
	datetime_modified = models.DateTimeField(auto_now = True ,verbose_name = _("Product Modified At"))
	
	def __str__(self):
		return f'name of product : {self.title}'
	
	def get_absolute_url(self):
		# برو به  صفحه ی product_details و آی‌دی محصولِ  رو بفرست!
		return reverse('product_details' , args = [self.pk])

# todo :  کلا کار Custom Manager اینست که اون درخواستهای (کوئری) ما که مد نظر ماست را بصورت پیشفرض اجرا میکنه
class ActiveCommentManager(models.Manager):
	""" یک Custom Manager برای active/deavtivation فیلد
	status_cmmnt = models.BooleanField(default = True)
	در table(کلاس) Comment"""
	def get_queryset(self):
		return super(ActiveCommentManager, self).get_queryset().filter(status_cmmnt = True)
	
class Comment(models.Model):
	product_cmmnt = models.ForeignKey(
		Product, on_delete = models.CASCADE, related_name = 'rel_prdct_cmmnts'
	, verbose_name = _("Product's Comment"),)
	author_cmmnt = models.ForeignKey(
		get_user_model(), on_delete = models.CASCADE, related_name = 'rel_athr_cmmnt'
	, verbose_name = _("Comment's Author"))
	cmmnt_body_txt = models.TextField(verbose_name = _("Comment's Text"))
	PRODUCT_STARS = [
		("1", _('Very Bad')),
		("2", _('Bad')),
		("3", _('Normal')),
		("4", _('Good')),
		("5", _('Perfect')),
	]
	stars_point_prdct = models.CharField(max_length = 10 , choices = PRODUCT_STARS ,
	verbose_name = _("What's Your Comment's Point Stars"))
	cmmnt_created_at = models.DateTimeField(auto_now_add = True, verbose_name = _("Comment Created At"))
	cmmnt_modified_at = models.DateTimeField(auto_now = True, verbose_name = _("Comment Modified At"))
	
	# Comment.objects.filter(active=True) : objects همان  Default Manager است
	# Comment.active_cmmnts_manager       : Custom Manager or Comment.xxx یا هر چیز دیگری میتوان نوشت
	""" ساخت Custom Manager برای status_cmmnt در بالای کلاس کامنت میباشد """
	status_cmmnt = models.BooleanField(default = True , verbose_name = _("Confirmed Comment"),)
	
	
	# Manager ها :
	objects = models.Manager() # : default manager
	status_cmmnt_manager = ActiveCommentManager # : Custom Manager
	
	def get_absolute_url(self) :
		# به جای اینکه self.pk (آی‌دی کامنت) رو بفرستی، آی‌دی محصولِ کامنت رو بفرست!
		return reverse('product_details' , args = [self.product_cmmnt.pk])
