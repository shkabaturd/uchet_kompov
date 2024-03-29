# Generated by Django 3.0.2 on 2020-01-17 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_number', models.CharField(default='', max_length=20, verbose_name='Инвентарный номер')),
                ('manufacturer', models.CharField(default='', max_length=20, verbose_name='Производитель')),
                ('owner', models.CharField(default='', max_length=20, verbose_name='Материально ответственный')),
                ('last_service_date', models.DateTimeField(verbose_name='Дата последней проверки')),
                ('status', models.BooleanField(default=True, verbose_name='Иправность')),
            ],
            options={
                'verbose_name': 'Компьютер',
                'verbose_name_plural': 'Компьютеры',
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(default='', max_length=20, verbose_name='Серийный номер')),
                ('manufacturer', models.CharField(default='', max_length=20, verbose_name='Производитель')),
                ('physical_size', models.CharField(max_length=8, verbose_name='Фромфактор')),
                ('amount', models.IntegerField(default=0, verbose_name='Размер (Гб)')),
                ('ram_type', models.CharField(max_length=6, verbose_name='Тип')),
                ('speed', models.IntegerField(default=0, verbose_name='Скорость (Ггц)')),
                ('status', models.BooleanField(default=True, verbose_name='Иправность')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uchet.Computer', verbose_name='Компьютер')),
            ],
            options={
                'verbose_name': 'Оперативная память',
                'verbose_name_plural': 'Оперативная память',
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(default='', max_length=20, verbose_name='Серийный номер')),
                ('manufacturer', models.CharField(default='', max_length=20, verbose_name='Производитель')),
                ('hdd_type', models.CharField(max_length=6, verbose_name='Фромфактор')),
                ('capacity', models.IntegerField(default=0, verbose_name='Объём (Гб)')),
                ('speed', models.IntegerField(default=0, verbose_name='Скорость')),
                ('status', models.BooleanField(default=True, verbose_name='Иправность')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uchet.Computer', verbose_name='Компьютер')),
            ],
            options={
                'verbose_name': 'Жесткий диск',
                'verbose_name_plural': 'Жесткие диски',
            },
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(default='', max_length=20, verbose_name='Серийный номер')),
                ('manufacturer', models.CharField(default='', max_length=20, verbose_name='Производитель')),
                ('socket', models.CharField(max_length=8, verbose_name='Сокет')),
                ('freequency', models.IntegerField(default=0, verbose_name='Частота')),
                ('cores', models.IntegerField(default=0, verbose_name='Количество ядер')),
                ('status', models.BooleanField(default=True, verbose_name='Иправность')),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uchet.Computer', verbose_name='Компьютер')),
            ],
            options={
                'verbose_name': 'Процессор',
                'verbose_name_plural': 'Процессоры',
            },
        ),
    ]
