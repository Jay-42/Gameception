# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-04 18:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0043_auto_20160604_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosassinatura',
            name='precoPorJogo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='numero',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
