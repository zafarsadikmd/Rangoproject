# Generated by Django 4.2.5 on 2023-09-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RANGO', '0004_rename_landnmark_register_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
