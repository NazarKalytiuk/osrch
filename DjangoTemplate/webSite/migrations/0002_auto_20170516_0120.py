# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-15 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webSite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pib', models.CharField(max_length=300)),
                ('passportInfo', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13)),
                ('inn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('UAH', 'Hryvnia'), ('USD', 'Dollar USA'), ('EUR', 'Euro'), ('RUB', 'Russian ruble')], default='UAH', max_length=3)),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('periodDays', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('persent', models.DecimalField(decimal_places=3, max_digits=4)),
                ('isClosed', models.NullBooleanField()),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webSite.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pib', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=100)),
                ('salary', models.BigIntegerField()),
                ('requirenments', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.AddField(
            model_name='deposit',
            name='employeeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webSite.Employee'),
        ),
    ]
