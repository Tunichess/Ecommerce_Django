# Generated by Django 2.0.3 on 2020-04-21 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_billing_address_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address_final',
            field=models.TextField(blank=True, null=True),
        ),
    ]
