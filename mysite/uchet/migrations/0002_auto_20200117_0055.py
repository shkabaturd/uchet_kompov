# Generated by Django 3.0.2 on 2020-01-16 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uchet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='cpu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uchet.CPU', verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='hdd',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uchet.HDD', verbose_name='Жесткий диск'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='ram',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uchet.RAM', verbose_name='Оперативная память'),
        ),
    ]
