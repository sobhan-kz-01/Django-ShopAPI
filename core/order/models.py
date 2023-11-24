from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from settings.models import BaseModel

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
