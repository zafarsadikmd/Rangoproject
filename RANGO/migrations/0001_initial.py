# Generated by Django 4.2.5 on 2023-09-29 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurantname', models.CharField(max_length=150)),
                ('EmailId', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('locality', models.CharField(max_length=200)),
                ('landnmark', models.CharField(max_length=200)),
                ('contact', models.IntegerField(max_length=12)),
                ('date', models.DateField(verbose_name='')),
            ],
        ),
    ]
