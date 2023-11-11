from django.db import models
from uuid import uuid4
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.models import Manager

class BaseModelManager(Manager):
    def all_active_objects(self):
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
        verbose_name=_("Is Active?"), default=True,editable=False
    )
    uuid = models.UUIDField(verbose_name="UUID", default=uuid4, editable=False)
    objects = BaseModelManager()
    class Meta:
        abstract = True
