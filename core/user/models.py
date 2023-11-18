from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from settings.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    number = models.CharField(verbose_name=_("Number"), max_length=20)
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)

    def __str__(self) -> str:
        if self.user.email:

            return self.user.email
        return self.user.username
