# Generated by Django 4.0.6 on 2022-09-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_return', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreturn',
            name='status',
            field=models.BooleanField(),
        ),
    ]
