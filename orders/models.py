from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """اطلاعات خریدار، نشانی و وضعیت پرداخت یک سفارش را نگه می‌دارد."""

    # کاربری که سفارش را ثبت کرده است.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
	    verbose_name = _('User')
    )

    # وضعیت پرداخت؛ سفارش جدید به‌صورت پیش‌فرض پرداخت‌نشده است.
    is_paid = models.BooleanField(default=False,  verbose_name = _('IsPaid'))

    # اطلاعات گیرنده و نشانی ثبت‌شده برای همین سفارش.
    first_nm = models.CharField(max_length=100,  verbose_name = _('First Name'))
    last_nm = models.CharField(max_length=100,  verbose_name = _('Last Name'))
    phone_nmbr = models.CharField(max_length=15, verbose_name = _('Phone Number'))
    address = models.TextField(max_length=700,  verbose_name = _('Address'))

    # توضیحات اختیاریِ همراه سفارش.
    order_notes = models.TextField(blank=True,  verbose_name = _('Order Notes'))

    # زمان ایجاد سفارش و زمان آخرین ذخیرهٔ آن.
    dttm_created_at = models.DateTimeField(auto_now_add=True , verbose_name = _("Created Date at"))
    dttm_modified_at = models.DateTimeField(auto_now=True, verbose_name = _("Modified Date at"))

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
        verbose_name = _("Order's Items")
    )

    # محصول انتخاب‌شده در این ردیف سفارش.
    prdct_ordr = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="prdct_rel_ordr",
        verbose_name = _("Product of Order's Items")
    )

    # تعداد محصول در این ردیف باید دست‌کم یک عدد باشد.
    qntt_prdct_ordr = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
	    verbose_name = _("Product's Quantity of Order's Items")
    )

    # قیمت ثبت‌شده برای یک واحد محصول در این ردیف؛ واحد پول را پروژه تعیین می‌کند.
    price_prdct_ordr = models.PositiveIntegerField(default=1,
        validators=[MinValueValidator(1)],
        verbose_name = _("Product's Price of Order's Items")
        )

    # زمان ایجاد ردیف سفارش و زمان آخرین ذخیرهٔ آن.
    prdct_ordr_created_at = models.DateTimeField(auto_now_add=True)
    prdct_ordr_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """خلاصهٔ خوانای ردیف سفارش را برمی‌گرداند."""
        
        return f'OrderItem with ID: {self.id}: for Pruduct {self.prdct_ordr} X {self.qntt_prdct_ordr} \
	        	with Pice : {self.price_prdct_ordr}'
            # f"ردیف سفارش {self.pk}: محصول {self.prdct_ordr_id} × "
            # f"{self.qntt_prdct_ordr}، قیمت واحد: {self.price_prdct_ordr}"
        

	
		