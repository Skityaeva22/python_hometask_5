# Generated by Django 5.0.6 on 2024-05-07 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_depositor_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depositor',
            name='birthday',
        ),
    ]
