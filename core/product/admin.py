from django.contrib import admin
from .models import Product, Category, ProductInventory, Varient, VarientTitle


@admin.register(VarientTitle)
class VarientTitleAdmin(admin.ModelAdmin):
    list_display = ["title", "varient_type"]
    list_filter = ["title", "varient_type"]


@admin.register(Varient)
class VarientAdmin(admin.ModelAdmin):
    list_filter = ["title", "value", "color", "color_name"]
    list_display = ["title", "value", "color_name"]
    search_fields = ["value", "color_name", "color"]


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_filter = ["product"]
    list_display = ["product", "quantity"]


class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1
    autocomplete_fields = ["varients"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductInventoryInline,)
    list_display = ["__str__", "unit_price", "id"]
    list_filter = ["title", "description", "id", "unit_price"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id"]
    list_filter = ["title", "id"]
