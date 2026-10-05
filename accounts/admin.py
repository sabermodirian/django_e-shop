from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm , CustomUserCreationForm
from .models import CustomUser    # == from accounts.models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	List_display = ('email' , 'username',)