from django.db import models
from django.template.defaultfilters import title


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