# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-25 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_auto_20171225_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id_board_post_parent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]