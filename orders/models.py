from django.conf import settings
from django.db import models


class Order(models.Model):
    """اطلاعات ثبت سفارش، خریدار و وضعیت پرداخت را نگه می‌دارد."""

    # ارتباط سفارش با کاربری که آن را ثبت کرده است.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # سفارش تا پیش از ثبت پرداخت، پرداخت‌نشده در نظر گرفته می‌شود.
    is_paid = models.BooleanField(default=False)

    # اطلاعات تماس و نشانیِ ثبت‌شده برای این سفارش.
    first_nm = models.CharField(max_length=100)
    last_nm = models.CharField(max_length=100)
    phone_nmbr = models.CharField(max_length=15)
    address = models.CharField(max_length=700)

    # زمان ایجاد سفارش و آخرین ذخیرهٔ آن.
    dttm_created_at = models.DateTimeField(auto_now_add=True)
    dttm_modified_at = models.DateTimeField(auto_now=True)
