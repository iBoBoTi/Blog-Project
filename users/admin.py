from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff',]

admin.site.register(CustomUser, CustomUserAdmin)