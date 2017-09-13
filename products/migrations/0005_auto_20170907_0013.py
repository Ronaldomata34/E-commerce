# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 00:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_platform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platform_of_product', to='products.Platform'),
        ),
    ]