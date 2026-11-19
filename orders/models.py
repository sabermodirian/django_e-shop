from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    """اطلاعات خریدار، نشانی و وضعیت پرداخت یک سفارش را نگه می‌دارد."""

    # کاربری که سفارش را ثبت کرده است.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # وضعیت پرداخت؛ سفارش جدید به‌صورت پیش‌فرض پرداخت‌نشده است.
    is_paid = models.BooleanField(default=False)

    # اطلاعات گیرنده و نشانی ثبت‌شده برای همین سفارش.
    first_nm = models.CharField(max_length=100)
    last_nm = models.CharField(max_length=100)
    phone_nmbr = models.CharField(max_length=15)
    address = models.CharField(max_length=700)

    # توضیحات اختیاریِ همراه سفارش.
    order_notes = models.TextField(blank=True)

    # زمان ایجاد سفارش و زمان آخرین ذخیرهٔ آن.
    dttm_created_at = models.DateTimeField(auto_now_add=True)
    dttm_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """شناسهٔ خوانای سفارش را برمی‌گرداند."""
        return f"سفارش شماره {self.pk}"


class OrderItem(models.Model):
    """یک ردیف سفارش شامل محصول، تعداد و قیمت ثبت‌شده را نگه می‌دارد."""

    # سفارشی که این ردیف به آن تعلق دارد.
    itms_ordr = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="items_rel_ordr",
    )

    # محصول انتخاب‌شده در این ردیف سفارش.
    prdct_ordr = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="prdct_rel_ordr",
    )

    # تعداد محصول در این ردیف باید دست‌کم یک عدد باشد.
    qntt_prdct_ordr = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
    )

    # قیمت ثبت‌شده برای یک واحد محصول در این ردیف؛ واحد پول را پروژه تعیین می‌کند.
    price_prdct_ordr = models.PositiveIntegerField(default=1,
        validators=[MinValueValidator(1)],)

    # زمان ایجاد ردیف سفارش و زمان آخرین ذخیرهٔ آن.
    prdct_ordr_created_at = models.DateTimeField(auto_now_add=True)
    prdct_ordr_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """خلاصهٔ خوانای ردیف سفارش را برمی‌گرداند."""
        
        return f'OrderItem wit ID: {self.id}: for Pruduct {self.prdct_ordr} X {self.qntt_prdct_ordr} \
	        	with Pice : {self.price_prdct_ordr}'
            # f"ردیف سفارش {self.pk}: محصول {self.prdct_ordr_id} × "
            # f"{self.qntt_prdct_ordr}، قیمت واحد: {self.price_prdct_ordr}"
        

	
		