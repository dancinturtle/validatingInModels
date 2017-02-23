# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-23 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manyToMany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habitat', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='pets',
            field=models.ManyToManyField(related_name='userpet', to='manyToMany.Pet'),
        ),
    ]
