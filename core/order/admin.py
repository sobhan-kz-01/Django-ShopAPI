from django.contrib import admin
from .models import Cart, CartItem, Coupon

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_filter = ['is_active','user']
    list_display = ['__str__','is_active','created_at','id']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_filter = ['code','valid_from','valid_to']
    list_display = ['code','valid_from','valid_to']
