# Generated by Django 5.0.6 on 2024-05-07 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_deposit_dc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='dc',
        ),
    ]
