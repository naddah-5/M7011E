from django.contrib import admin
from .models import Product
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from webstore.models import UserProfile, Product, Order

# Register your models here.
admin.site.register(Permission)
admin.site.unregister(get_user_model())

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(BaseUserAdmin):
    inlines = [
        UserProfileInline,
    ]

# Super user
admin.site.register(get_user_model(), UserAdmin)

# Admin
# Super User needs to set permission for Admin to view/edit these models
# TODO: Add all the models
admin.site.register(Product)
admin.site.register(Order)