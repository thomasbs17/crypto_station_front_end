# Generated by Django 5.0 on 2023-12-11 01:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crypto_station_api", "0005_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trades",
            fields=[
                (
                    "trade_dim_key",
                    models.CharField(
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Trade Record ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=36, verbose_name="User ID")),
                ("trade_id", models.CharField(max_length=36, verbose_name="Trade ID")),
                (
                    "order_id",
                    models.CharField(max_length=36, verbose_name="Related Order ID"),
                ),
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
                    "trade_side",
                    models.CharField(
                        choices=[("buy", "Buy"), ("sell", "Sell")],
                        max_length=4,
                        verbose_name="Trade Side",
                    ),
                ),
                (
                    "execution_tmstmp",
                    models.DateTimeField(verbose_name="Trade Execution Timestamp"),
                ),
                ("trade_volume", models.FloatField(verbose_name="Trade Volume")),
                ("order_price", models.FloatField(verbose_name="Trade Price")),
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
