# Generated by Django 4.2.5 on 2023-09-30 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RANGO', '0002_alter_register_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='date',
        ),
    ]
