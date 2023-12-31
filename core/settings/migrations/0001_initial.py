# Generated by Django 4.2.7 on 2023-11-26 07:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
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
                    "payment_method",
                    models.CharField(
                        blank=True,
                        choices=[("PAYPAL", "Paypal"), ("ZARINPALL", "Zarinpall")],
                        max_length=200,
                        null=True,
                        verbose_name="Payment Method",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="settings", verbose_name="Logo"
                    ),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True, max_length=1000, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Number"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
