# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 11:35
from __future__ import unicode_literals

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='/static/img/default.jpg', force_format='JPEG', keep_meta=True, quality=0, size=[250, 250], upload_to='profile_pics'),
        ),
    ]
