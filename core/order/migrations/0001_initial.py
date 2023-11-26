# Generated by Django 4.2.7 on 2023-11-25 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("product", "0004_alter_product_discount_type_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="Is Active?"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, verbose_name="UUID"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Coupon",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="Is Active?"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, verbose_name="UUID"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        default=order.models.char_generator,
                        max_length=30,
                        unique=True,
                        verbose_name="Coupon code",
                    ),
                ),
                (
                    "value",
                    models.BigIntegerField(
                        default=10,
                        help_text="Percentage value",
                        verbose_name="Coupon value",
                    ),
                ),
                ("valid_from", models.DateField(verbose_name="Valid from")),
                ("valid_to", models.DateField(verbose_name="Valid to")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, editable=False, verbose_name="Is Active?"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, verbose_name="UUID"
                    ),
                ),
                ("quantity", models.PositiveBigIntegerField(verbose_name="Quantity")),
                (
                    "cart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order.cart",
                        verbose_name="Cart",
                    ),
                ),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.productinventory",
                        verbose_name="Product Inventory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]