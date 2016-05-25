# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assinante', '0015_auto_20160525_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosassinatura',
            name='assinatura',
        ),
        migrations.RemoveField(
            model_name='dadosbancarios',
            name='assinatura',
        ),
        migrations.RemoveField(
            model_name='enderecoassinatura',
            name='assinatura',
        ),
        migrations.AddField(
            model_name='assinante',
            name='dAssinatura',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.DadosAssinatura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinante',
            name='dBanco',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.DadosBancarios'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assinante',
            name='endAssinatura',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='Assinante.EnderecoAssinatura'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]