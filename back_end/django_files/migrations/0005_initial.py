# Generated by Django 5.0 on 2023-12-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("crypto_station_api", "0004_delete_orders"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "order_dim_key",
                    models.CharField(
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Order Record ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=36, verbose_name="User ID")),
                ("order_id", models.CharField(max_length=36, verbose_name="Order ID")),
                (
                    "broker_id",
                    models.CharField(max_length=36, verbose_name="Broker ID"),
                ),
                (
                    "trading_env",
                    models.CharField(
                        choices=[("paper_trading", "Paper Trading"), ("live", "Live")],
                        max_length=13,
                        verbose_name="Live or Paper Trading",
                    ),
                ),
                (
                    "trading_type",
                    models.CharField(
                        choices=[("spot", "Spot"), ("derivative", "Derivative")],
                        max_length=10,
                        verbose_name="Spot or Derivatives",
                    ),
                ),
                ("asset_id", models.CharField(max_length=36, verbose_name="Asset ID")),
                (
                    "order_side",
                    models.CharField(
                        choices=[("buy", "Buy"), ("sell", "Sell")],
                        max_length=4,
                        verbose_name="Order Side",
                    ),
                ),
                (
                    "order_type",
                    models.CharField(
                        choices=[("limit", "Limit"), ("market", "Market")],
                        max_length=6,
                        verbose_name="Order Type",
                    ),
                ),
                (
                    "order_creation_tmstmp",
                    models.DateTimeField(verbose_name="Order Creation Timestamp"),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("open", "Open"),
                            ("executed", "Executed"),
                            ("cancelled", "Cancelled"),
                        ],
                        max_length=9,
                        verbose_name="Order Status",
                    ),
                ),
                ("fill_pct", models.FloatField(verbose_name="Fill Percentage")),
                ("order_volume", models.FloatField(verbose_name="Order Volume")),
                ("order_price", models.FloatField(verbose_name="Order Price")),
                (
                    "insert_tmstmp",
                    models.DateTimeField(verbose_name="Record Insert Timestamp"),
                ),
                (
                    "expiration_tmstmp",
                    models.DateTimeField(
                        null=True, verbose_name="Record Expiration Timestamp"
                    ),
                ),
            ],
        ),
    ]