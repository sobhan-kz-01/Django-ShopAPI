from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from settings.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    number = models.CharField(verbose_name=_("Number"), max_length=20)
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)

    def __str__(self) -> str:
        return str(self.user)


class UserAddress(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    state = models.CharField(verbose_name=_("State"), max_length=400)
    city = models.CharField(verbose_name=_("City"), max_length=400)
    address = models.TextField(verbose_name=_("Address"))
    number = models.CharField(verbose_name=_("Number"), max_length=40)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name_plural = _("User Addresses")
        verbose_name = _("User Address")
