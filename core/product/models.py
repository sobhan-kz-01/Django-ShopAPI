from django.db import models
from django.utils.translation import gettext_lazy as _
from settings.models import BaseModel


class Product(BaseModel):
    """
    Product table in database
    """

    title = models.CharField(max_length=400, verbose_name=_("Title"))
    price = models.PositiveBigIntegerField(verbose_name=_("Price"))
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    category = models.ForeignKey(
        "product.Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title


class Category(BaseModel):
    """
    Category table in database
    """

    title = models.CharField(max_length=400, verbose_name=_("Title"))

    def __str__(self) -> str:
        return self.title
