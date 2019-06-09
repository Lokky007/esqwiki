# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-06-08 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectTasks',
            fields=[
                ('id_project_task', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2048)),
                ('complete_percentage', models.IntegerField()),
                ('finished', models.BooleanField(default=0)),
                ('x_created', models.DateTimeField(auto_now_add=True)),
                ('x_modified', models.DateTimeField(auto_now=True)),
                ('x_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]