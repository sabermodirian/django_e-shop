


class Cart:
	def __init__(self, request):
		self.request = request
		self.session = request.session
		
		cart = self.session.get('cart_obj') # اگر در session  شیئ cart وجود داشت بریزش داخل متغیر cart
		
		if not cart: # اگر شیئ cart در session مربوطه به این request کاربر وجود نداشت :
			self.session['cart_obj'] = {} # بیا و یک cart در این session آمده از کاربر جدید بساز و فعلا خالی {} بگذار
			cart = self.session['cart_obj'] # حالا این cart خالی تازه ساخته شده در session رو بریزش در همون متغیر cart
		
		"""
		cart = self.session.setdefault('cart_obj', {})  #معادل سه خط بالا در یک خط
		setdefault میگه:
			اگر 'cart_obj' توی session وجود داشت → همان را بده
			اگر نبود → بسازش با {} و همان را بده
			یعنی دقیقاً معادل همان سه خط توست.
		"""
		self.cart = cart
		

