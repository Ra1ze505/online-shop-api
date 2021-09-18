# Generated by Django 3.2.5 on 2021-08-30 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Цвет')),
                ('slug', models.SlugField(default='', verbose_name='Ссылка')),
                ('code', models.CharField(max_length=7, verbose_name='Код цвета')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Контейнер',
                'verbose_name_plural': 'Контейнеры',
            },
        ),
        migrations.CreateModel(
            name='Сonsist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Состав')),
            ],
            options={
                'verbose_name': 'Состав',
                'verbose_name_plural': 'Составы',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('category', models.ManyToManyField(blank=True, to='main.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='CollectionForProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('production', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='main.production', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Колекция',
                'verbose_name_plural': 'Колекции',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='container',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.container', verbose_name='Контейнер'),
        ),
    ]
