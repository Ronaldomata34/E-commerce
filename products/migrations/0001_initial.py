# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('disparo', 'disparo'), ('carrera', 'carrera'), ('terror', 'terror'), ('deporte', 'deporte')], max_length=255)),
                ('console', models.CharField(choices=[('Ps4', 'Ps4'), ('Ps3', 'Ps3')], max_length=255)),
                ('type_game', models.CharField(choices=[('Season Pass', 'Season Pass'), ('DLC', 'DLC'), ('Full Game', 'Full Game')], max_length=100)),
                ('hard_disk_space', models.IntegerField()),
                ('language', models.CharField(max_length=255)),
                ('available', models.BooleanField(default=True)),
                ('offer', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
    ]