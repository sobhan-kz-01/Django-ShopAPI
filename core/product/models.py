from django.db import models
from django.utils.translation import gettext_lazy as _
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
        PERCENTAGE = _("Percentage")
        VALUE = _("Value") 


    title = models.CharField(max_length=400, verbose_name=_("Title"))
    price = models.PositiveBigIntegerField(verbose_name=_("Price"))
    image = models.ImageField(verbose_name=_("Image"), null=True, blank=True)
    description = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    
    is_digital = models.BooleanField(verbose_name=_("Is digital product?"),default=False)
    categories = models.ManyToManyField(Category,verbose_name=_("Categories"),blank=False)
    discount = models.PositiveBigIntegerField(_('تخفیف'),null=True,blank=True)
    discount_type = models.CharField(choices=ProductDiscountChoices.choices,max_length=70,blank=True,null=True,verbose_name='نوع تخفیف')

    
    
    def __str__(self) -> str:
        return self.title


class Varient(BaseModel):
    quantity = models.PositiveBigIntegerField(verbose_name=_("Quantity"))


