# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-18 21:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('views', models.IntegerField(default=0)),
                ('tag', models.CharField(blank=True, max_length=30, null=True)),
                ('likes', models.IntegerField(default=0)),
                ('status', models.IntegerField(choices=[(1, 'To Do'), (2, 'Doing'), (3, 'Done'), (4, 'Wont fix')], default=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BugComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('text', models.TextField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bugs.Bug')),
            ],
            options={
                'ordering': ('created_date',),
            },
        ),
        migrations.CreateModel(
            name='BugLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_bug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.Bug')),
                ('liker_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]