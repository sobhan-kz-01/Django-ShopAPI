from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField

from settings.models import BaseModel, SeoAbstract

class Category(BaseModel, SeoAbstract):
    """
    Category table in database
    """

    title = models.CharField(max_length=400, verbose_name=_("Title"))

    def __str__(self) -> str:
        return self.title


class Product(BaseModel, SeoAbstract):
    """
    Product table in database
    """

    class ProductDiscountChoices(models.TextChoices):
        PERCENTAGE = _("PERCENTAGE")
        VALUE = _("VALUE")

    title = models.CharField(max_length=400, verbose_name=_("Title"))
    unit_price = models.PositiveBigIntegerField(verbose_name=_("Price"))
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)

    is_digital = models.BooleanField(
        verbose_name=_("Is digital product?"), default=False
    )
    categories = models.ManyToManyField(
        Category, verbose_name=_("Categories"), blank=False
    )
    discount = models.PositiveBigIntegerField(
        verbose_name=_("Discount"), null=True, blank=True
    )
    discount_type = models.CharField(
        choices=ProductDiscountChoices.choices,
        max_length=70,
        blank=True,
        null=True,
        verbose_name=_("Discount type"),
    )

    def __str__(self) -> str:
        return self.title


class VarientTitle(BaseModel):
    """
    Varient title table
    Usage:
        color / select
    Example:
        Sizes
        Product color
    """
    class VarientType(models.TextChoices):
        COLOR = _("COLOR")
        SELECT_BOX = _("SELECT BOX")

    title = models.CharField(verbose_name=_("Title"), max_length=400)
    varient_type = models.CharField(verbose_name=_("Varient type"), choices=VarientType.choices, max_length=100)

    def __str__(self) -> str:
        return self.title
    

class Varient(BaseModel):
    """
    Custom Varient value
    Example value:
        sizes:XXL,XL
    """
    title = models.ForeignKey(VarientTitle, on_delete=models.CASCADE, verbose_name=_("Varient Title"))
    value = models.CharField(verbose_name=_("Value"), max_length=400,null=True,blank=True)
    color = ColorField(verbose_name=_("Color"), null=True, blank=True)
    color_name = models.CharField(verbose_name=_("Color name"), max_length=300, null=True, blank=True)
    def __str__(self) -> str:
        if self.color_name:
            return self.color_name
        return self.value
    
    def clean(self) -> None:
        if self.color and not self.title.varient_type == "COLOR":
            raise ValidationError(_("Invalid varient type"))
        
        if self.value and self.title.varient_type == "COLOR":
            raise ValidationError(_("Invalid varient type"))
        
        
        if self.color_name and not self.color or self.color and not self.color_name:
            raise ValidationError(_("Should use color name and color at same time"))
        
        return super().clean()


class ProductInventory(BaseModel):
    """
    Inventory for products with different varients
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    quantity = models.PositiveBigIntegerField(verbose_name=_("Quantity"))
    varients = models.ManyToManyField(Varient, verbose_name=_("Varients"))
    price = models.PositiveBigIntegerField(verbose_name=_("Price"))

    def __str__(self) -> str:
        return self.product.title