# Generated by Django 5.0.5 on 2024-05-06 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankowner',
            options={'verbose_name': 'Владелец', 'verbose_name_plural': 'Владельцы'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.AlterModelOptions(
            name='deposit',
            options={'verbose_name': 'Вклад', 'verbose_name_plural': 'Вклады'},
        ),
        migrations.AlterModelOptions(
            name='depositor',
            options={'verbose_name': 'Вкладчик', 'verbose_name_plural': 'Вкладчики'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Персона', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.RemoveField(
            model_name='person',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='deposit',
            name='annual_percentage',
            field=models.FloatField(default=0.0, verbose_name='Годовой процент'),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=50, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='code',
            field=models.CharField(max_length=3, verbose_name='Кодовой обозначение'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.currency'),
        ),
    ]
