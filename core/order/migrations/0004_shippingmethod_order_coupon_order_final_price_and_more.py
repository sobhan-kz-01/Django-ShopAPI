# Generated by Django 4.2.7 on 2023-11-26 07:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_order_cart_order_status_order_user_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ShippingMethod",
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
                ("title", models.CharField(max_length=400, verbose_name="Title")),
                ("price", models.PositiveBigIntegerField(verbose_name="Price")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="order",
            name="coupon",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="order.coupon",
                verbose_name="Coupon",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="final_price",
            field=models.PositiveBigIntegerField(default=0, verbose_name="Final Price"),
        ),
        migrations.AddField(
            model_name="order",
            name="shipping_method",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="order.shippingmethod",
            ),
        ),
    ]