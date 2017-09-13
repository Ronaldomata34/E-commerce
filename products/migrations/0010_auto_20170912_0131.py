# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 01:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170912_0128'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'types of games',
                'ordering': ('name',),
                'verbose_name': 'type of game',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='typeofgame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_of_game', to='products.TypeOfGame'),
        ),
    ]