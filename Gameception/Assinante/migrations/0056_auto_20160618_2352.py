# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-19 02:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0055_auto_20160618_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='assinante',
            name='telefone',
            field=models.CharField(default=34846157, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
