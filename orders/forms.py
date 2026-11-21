from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = [ 'first_nm', 'last_nm', 'phone_nmbr', 'address','order_notes' ]
		