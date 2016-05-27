# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0031_auto_20160525_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
        migrations.AlterField(
            model_name='historicojogos',
            name='assinatura',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Assinante.Assinante'),
        ),
    ]
