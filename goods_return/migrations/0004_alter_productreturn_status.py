# Generated by Django 4.0.6 on 2022-09-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_return', '0003_alter_productreturn_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreturn',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]