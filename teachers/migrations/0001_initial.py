# Generated by Django 4.1.5 on 2023-02-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('birth_day', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('phone', models.CharField(max_length=14, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]