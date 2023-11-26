from django.contrib import admin
from user.models import Profile, UserAddress


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__", "id")
    list_filter = ("user", "id")


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_filter = ["user", "state", "city"]
    list_display = ["user", "state", "city"]
