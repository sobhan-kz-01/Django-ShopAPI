from django.contrib import admin
from user.models import Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("__str__","id")
    list_filter = ("user","id")