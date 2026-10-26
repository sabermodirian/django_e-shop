from products.models import Product

'''
بدان وآگاه باش که هربار که یک شیئ ازین کلاس Cart میسازیم
 یعنی یک سبد خرید برای آن کاربرخاص ایجاد میشود ولی
    تذکر: برای هر کاربر فقط یک سشن ایجاد میشود
 اگر حتی 1000 تا ریکویست هم برای هر سبد خرید یک کاربر
  بفرستیم همه در یک سشن قرار میگیرند
'''

class Cart:
    """🛒 Manage the user's shopping cart inside Django session."""
    
    def __init__(self, request):
	    # Initialize Cart class
        self.request = request
        self.session = request.session
        
        cart = self.session.get('cart_obj')  # اگر در session شیئ cart وجود داشت بریزش داخل متغیر cart
        
        if not cart:  # اگر شیئ cart در session مربوطه به این request کاربر وجود نداشت :
            self.session['cart_obj'] = {}  # بیا و یک cart در این session آمده از کاربر جدید بساز و فعلا خالی {} بگذار
            cart = self.session['cart_obj']  # حالا این cart خالی تازه ساخته شده در session رو بریزش در همون متغیر cart
            # cart = self.session['cart_obj'] = {}  ترکیب دوخط بالا و صحیح هم میباشد
            
        # 💡 حواست باشه این بخش به جای بلاک چندخطی (که وسط کد به عنوان کامنت اجرا می‌شد)
        # به صورت کامنت تک‌خطی یا با ایندنت درست قرار گرفت تا پایتون گیر نده:
        """
        cart = self.session.setdefault('cart_obj', {})  <-- معادل سه خط بالا در یک خط
        setdefault میگه:
        اگر 'cart_obj' توی session وجود داشت → همان را بده
        اگر نبود → بسازش با {} و همان را بده
        یعنی دقیقاً معادل همان سه خط بالاست.
        """
        self.cart = cart
        
    def add_prdct(self, product, quantity=1):
	    """ Add the specified product to the Cart if it exists """
	    # اینجا متد اضافه‌کردن محصول رو جلو می‌بریم...
	    prdct_id = str(product.id)
	    
	    if prdct_id not in self.cart :  # محصول با شماره آِیدی (prdct_id) به تعداد quantity برای کاربر ذخیره میشود
		    self.cart[prdct_id] = {
			    'quantity' : quantity}  # پس سبدخرید به صورت پیشفرض یک دیکشنریست که کلید آن (prdct_id) محصول(حتما باید پر شده باشد) و مقدارش به عنوان  (تعداد  quantity که میتواند خالی هم باشد) در نظر گرفته و ذخیره میشود
	    # را نمیتوانیم درینجا اضافه کنیم زیرا اگر قیمت تغییر کند همچنان با قیمت قدیم در سبد نمایان میشود و برای اینکار باید قیمت را در لحظه ی خرید به دیتابیس رفته و بیرون بکشیم و محاسبه و نمایش دهیم : price
	    else :
		    # اگر ازقبل محصول وجود داشت در سبد خرید پس تعداد جدید را با تعداددرخواستی قبلی جمع میکنیم
		    self.cart[prdct_id]['quantity'] += quantity
		    # هر جا بعداً self.cart سبد خرید را تغییر دادی، این خط را فراموش نکن, و حتما session را آپدیت کن و حتما متد save را فراخوانی کن :
	    self.save()
     
        
    def remove_prdct(self, product):
	    """ Remove a product from the Cart"""
	    prdct_id = str(product.id)
	    if  prdct_id in self.cart:
		    del self.cart[prdct_id]
		    self.save()
    
    def save(self) :
	    """
		💾 ذخیره تغییرات سبد خرید در سشن
		هر جا self.cart تغییر کرد، این متد رو صدا می‌زنیم تا سشن ذخیره بشه.

		Save cart modifications to the session.
		"""
	    self.session.modified = True
    
    def __iter__(self) :
	    """
		🔄 قابلیت پیمایش (Iterate) روی سبد خرید
		محصولات واقعی رو از دیتابیس می‌کشه و با سبد خرید ترکیب می‌کنه.

		Make the cart iterable and attach actual Product objects to cart items.
		"""
	    prdct_ids = self.cart.keys()
	    products_objs = Product.objects.filter(id__in = prdct_ids)
	    
	    # یه کپی می‌گیریم تا موقع چرخش داده‌های اصلی سشن ناخواسته دستکاری نشن
	    cart_obj_cln = self.cart.copy()  # clone of Cart's object
	    
	    for product in products_objs :
		    cart_obj_cln[str(product.id)]['prdct_yld_obj'] = product
	    
	    for item in cart_obj_cln.values() :
		    item['total_price'] = item['prdct_yld_obj'].price * item['quantity']
		    yield item  # Generator
    
    def __len__(self) :
	    """ در اینجا منظور از len تعداد هر محصول موجود در سبد خرید میباشد"""
	    return len(self.cart.keys())
    
    def clear_cart(self) :
	    """ برای پاک کردن محصولات از سبد خرید"""
	    del self.session['cart_obj']
	    self.save()
    
    def get_total_price_prdcts(self) :
	    """
		💰 محاسبه مجموع کل قیمت محصولات در سبد خرید

		Calculate the total price of all items inside the cart.
		"""
	    # راه درست: استفاده از مقادیر ذخیره شده در سشن یا پیمایش روی کلاس
	    return sum(item['product'].price * item['quantity'] for item in self)
		
	 