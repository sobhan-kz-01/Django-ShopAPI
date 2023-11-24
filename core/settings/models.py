from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager


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