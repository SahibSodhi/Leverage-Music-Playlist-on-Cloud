# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaana', '0006_auto_20171016_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gaana.Album')),
            ],
        ),
    ]
