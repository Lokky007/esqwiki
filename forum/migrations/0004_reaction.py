# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-06 16:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0003_category_id_category_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id_reaction', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=2048)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('deleted', models.BooleanField(default=False)),
                ('x_created', models.DateTimeField(auto_now_add=True)),
                ('x_modified', models.DateTimeField(auto_now=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Answer')),
                ('x_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]