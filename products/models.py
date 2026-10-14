
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	price = models.PositiveIntegerField(default = 0)
	active = models.BooleanField(default = True)
	# cover_prdct = models.ImageField()
	datetime_created = models.DateTimeField(auto_now_add = True)
	datetime_modified = models.DateTimeField(auto_now = True)
	
	def __str__(self):
		return f'name of product : {self.title}'
	
	def get_absolute_url(self):
		return reverse('product_details' , args = [self.pk])
	
class Comment(models.Model):
	product_cmmnt = models.ForeignKey(
		Product, on_delete = models.CASCADE, related_name = 'rel_prdct_cmmnts'
	)
	author_cmmnt = models.ForeignKey(
		get_user_model(), on_delete = models.CASCADE, related_name = 'rel_athr_cmmnt'
	)
	cmmnt_body_txt = models.TextField()
	PRODUCT_STARS = [
		("1",'Very Bad'),
		("2", 'Bad'),
		("3", 'Normal'),
		("4", 'Good'),
		("5", 'Perfect'),
	]
	stars_point_prdct = models.CharField(max_length = 10 , choices = PRODUCT_STARS)
	cmmnt_created_at = models.DateTimeField(auto_now_add = True)
	cmmnt_modified_at = models.DateTimeField(auto_now = True)
	status_cmmnt = models.BooleanField(default = True)
	
	def get_absolute_url(self):
		return reverse('product_details' , args = [self.pk])