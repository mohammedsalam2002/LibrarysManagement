# Generated by Django 4.1 on 2022-09-03 18:49

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
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_price_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('retal_period', models.IntegerField(blank=True, max_length=2, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('availble', 'availble'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('catagery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='LibM.category')),
            ],
        ),
    ]
