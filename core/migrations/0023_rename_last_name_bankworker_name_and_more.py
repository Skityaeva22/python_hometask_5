# Generated by Django 5.0.6 on 2024-05-07 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_bankworker_delete_deposit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bankworker',
            old_name='last_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='role',
        ),
        migrations.RemoveField(
            model_name='bankworker',
            name='telephone',
        ),
    ]
