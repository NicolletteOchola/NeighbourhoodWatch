# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-27 06:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import pyuploadcare.dj.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('bs_name', models.CharField(max_length=30)),
                ('about', tinymce.models.HTMLField()),
                ('bs_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bs_email', models.EmailField(max_length=254)),
                ('bs_pic', pyuploadcare.dj.models.ImageField()),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighborhood_name', models.CharField(max_length=30)),
                ('neighborhood_location', models.CharField(max_length=30)),
                ('neighborhood_pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('occupants_count', models.IntegerField(null=True)),
                ('police_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('health_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('description', tinymce.models.HTMLField(max_length=70)),
                ('post_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('post_pic', pyuploadcare.dj.models.ImageField()),
                ('post_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='app.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', pyuploadcare.dj.models.ImageField()),
                ('bio', tinymce.models.HTMLField()),
                ('neighborhood', models.ManyToManyField(to='app.Neighborhood')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='bs_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='app.Neighborhood'),
        ),
    ]
