# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 00:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assinante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ChaveDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DadosAssinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('atividade', models.BooleanField(default=False)),
                ('memRAM', models.IntegerField()),
                ('memVideo', models.IntegerField()),
                ('assinatura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Assinante.Assinante')),
            ],
        ),
        migrations.CreateModel(
            name='DadosBancarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCartao', models.CharField(max_length=20)),
                ('codigoSeguranca', models.IntegerField()),
                ('nomeTitular', models.CharField(max_length=200)),
                ('vencimento', models.CharField(max_length=200)),
                ('assinatura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Assinante.Assinante')),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoAssinatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('numeroRua', models.IntegerField()),
                ('complemento', models.CharField(max_length=200)),
                ('CEP', models.CharField(max_length=9)),
                ('assinatura', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Assinante.Assinante')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.IntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Processadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SistOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistOp', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dadosassinatura',
            name='generosPessoais',
            field=models.ManyToManyField(to='Assinante.Genero'),
        ),
        migrations.AddField(
            model_name='dadosassinatura',
            name='processador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.Processadores'),
        ),
        migrations.AddField(
            model_name='dadosassinatura',
            name='sistOp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assinante.SistOp'),
        ),
    ]
