# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-30 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_registeremail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registeremail',
            options={'verbose_name': '邮箱验证', 'verbose_name_plural': '邮箱验证'},
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(default=1, max_length=15, verbose_name='QQ号'),
            preserve_default=False,
        ),
    ]
