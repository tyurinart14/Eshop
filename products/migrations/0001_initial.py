# Generated by Django 4.0.6 on 2022-08-18 19:36

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
                ('name', models.CharField(max_length=24)),
                ('slug', models.SlugField(max_length=24)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.TextField(blank=True)),
                ('image2', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField(null=True)),
                ('slug', models.SlugField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('availability', models.BooleanField(null=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.category')),
            ],
        ),
    ]