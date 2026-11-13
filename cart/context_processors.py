from .cart import Cart

def cart_func(request):
	""" این تابع وقتی یک ریکویستی میآید (دریافت میکنه) سپس دیکشنری (جیسونی) برمیگردنه که کلیدش cart و مقدارش یک شیئی از کلاس Cart(سبد خرید) هستش  """
	return {'cart':Cart(request)}