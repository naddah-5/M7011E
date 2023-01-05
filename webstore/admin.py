from django.contrib import admin
from .models import Product
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from embed_video.admin import AdminVideoMixin

from webstore.models import UserProfile, Product, Order, Category, Subcategory, InCategory, InSubcategory, Video

# Register your models here.
admin.site.register(Permission)
admin.site.unregister(get_user_model())

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

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
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(InCategory)
admin.site.register(InSubcategory)
admin.site.register(Video, AdminVideo)