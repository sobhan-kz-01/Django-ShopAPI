from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from settings.models import BaseModel

def char_generator():
    return get_random_string(6)
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))

    def __str__(self):
        return str(self.user)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, verbose_name=_("Cart"), on_delete=models.CASCADE)
    product_inventory = models.ForeignKey("product.ProductInventory", on_delete=models.CASCADE, verbose_name=_("Product Inventory"))
    quantity = models.PositiveBigIntegerField(verbose_name=_("Quantity"))
    
    def __str__(self):
        return self.product_inventory.product.title


class Coupon(BaseModel):
    code = models.CharField(verbose_name=_("Coupon code"), max_length=30, default=char_generator, unique=True)
    value = models.BigIntegerField(verbose_name=_('Coupon value'), help_text=_("Percentage value") , default=10)
    valid_from = models.DateField(verbose_name=_("Valid from"))
    valid_to = models.DateField(verbose_name=_("Valid to"))

    def __str__(self):
        return self.code


class Order(BaseModel):
    class OrderChoices(models.TextChoices):
        PENDING = _("PENDING")
        SHIPPED = _("SHIPPED")
        ON_HOLD = _("ON_HOLD")
        COMPLETED = _("COMPLETED")
        REFUNDED = _("REFUNDED")
        PROCCESSING = _("PROCCESSING")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(verbose_name=_("Order Status"), max_length=100, choices=OrderChoices.choices)
    cart = models.ForeignKey(Cart , on_delete=models.SET_NULL, null=True)




