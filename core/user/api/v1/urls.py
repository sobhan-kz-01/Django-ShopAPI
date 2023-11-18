from .views import ChangePasswordAPIView
from django.urls import path


urlpatterns = [
    path("change-password", ChangePasswordAPIView.as_view(), name="change-password")
]
