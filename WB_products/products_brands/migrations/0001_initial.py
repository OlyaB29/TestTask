# Generated by Django 4.1.7 on 2023-03-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(unique=True, verbose_name='Артикул')),
                ('brand', models.CharField(max_length=500, verbose_name='Название бренда')),
                ('title', models.CharField(max_length=500, verbose_name='Название товара')),
            ],
        ),
    ]