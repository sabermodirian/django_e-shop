from django.db import models
from django.conf import settings
# Create your models here.

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	is_paid = frst_nm = models.BooleanField(default = False)
	
	first_nm = models.CharField(max_length = 100)
	last_nm = models.CharField(max_length = 100)
	phone_nmbr = models.CharField(max_length = 15)
	address = models.CharField(max_length = 700)
	
	dttm_created_at = models.DateTimeField(auto_now_add = True)
	dttm_modified_at = models.DateTimeField(auto_now = True)
	