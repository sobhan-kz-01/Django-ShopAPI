from collections.abc import Iterable
from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager
from django.core.exceptions import ValidationError


class BaseModelManager(Manager):
    def all_active_objects(self):
        """
        Return active objects -> filter(is_active=True)
        """
        return super().all().filter(is_active=True)


class BaseModel(models.Model):
    """
    Abstract model to add custom fields per model inheritance
    """

    created_at = models.DateTimeField(
        verbose_name=_("Created At"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"), auto_now=True, editable=False
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active?"), default=True, editable=False
    )
    uuid = models.UUIDField(verbose_name="UUID", default=uuid4, editable=False)
    objects = BaseModelManager()

    class Meta:
        abstract = True


class SeoAbstract(models.Model):
    """
    Abstract model to add seo fields per model inheritance
    """

    meta_title = models.CharField(
        verbose_name=_("Meta title"),
        max_length=400,
        help_text="Meta Title",
        null=True,
        blank=True,
    )
    meta_keywords = models.TextField(
        verbose_name=_("Meta keywords"),
        max_length=600,
        help_text="Meta Keywords",
        null=True,
        blank=True,
    )
    meta_description = models.TextField(
        verbose_name=_("Meta description"),
        max_length=600,
        help_text="Meta Description",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class Setting(BaseModel):
    class SettingPaymentChoices(models.TextChoices):
        PAYPAL = _("PAYPAL")
        ZARINPALL = _("ZARINPALL")

    payment_method = models.CharField(
        verbose_name=_("Payment Method"),
        max_length=200,
        null=True,
        blank=True,
        choices=SettingPaymentChoices.choices,
    )
    logo = models.ImageField(
        verbose_name=_("Logo"), upload_to="settings", blank=True, null=True
    )
    address = models.TextField(
        verbose_name=_("Address"), max_length=1000, null=True, blank=True
    )
    number = models.CharField(
        verbose_name=_("Number"), max_length=100, null=True, blank=True
    )

    def __str__(self):
        return "Setting"

    def clean(self, **kwargs) -> None:
        if Setting.objects.count() >= 1:
            raise ValidationError(_("Cant save more than one setting object"))
        return super().clean()
