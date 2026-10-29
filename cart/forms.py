from django import forms


class AddToCartProductForm(forms.Form):
    """
    🛒 فرم انتخاب تعداد محصول برای افزودن به سبد خرید
    Product Quantity Selection Form for Cart Addition

    این فرم به کاربر اجازه می‌دهد تعداد دلخواه از یک محصول (از ۱ تا ۳۰ عدد) را
    انتخاب کند تا به سبد خرید اضافه شود. از `TypedChoiceField` استفاده شده تا
    مقدار انتخاب‌شده به‌صورت خودکار به نوع دادهٔ `int` (عدد صحیح) تبدیل (coerce) شود.

    This form lets users choose the desired quantity of a product (from 1 to 30)
    to add to their cart. We use `TypedChoiceField` so that the selected value
    is automatically coerced and converted into an integer (`int`).
    """

    # 📊 ایجاد یک لیست از گزینه‌ها (Tuple) برای تعداد محصولات از ۱ تا ۳۰
    # Generate a list of choices tuples for product quantities from 1 to 30.
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]

    # 🔢 فیلد انتخاب تعداد با قابلیت تبدیل خودکار به عدد صحیح (Integer)
    # Quantity selection field with automatic coercion to integer.
    quantity = forms.TypedChoiceField(
	    choices = QUANTITY_CHOICES ,
	    coerce = int ,
	    label = "Quantity / تعداد" ,
    )
    
    inplace = forms.BooleanField(
	    required = False ,
	    widget = forms.HiddenInput
    )