# Generated by Django 3.0.2 on 2020-01-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0005_computer_computer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='comment',
            field=models.TextField(default='', verbose_name='Комментарий'),
        ),
    ]