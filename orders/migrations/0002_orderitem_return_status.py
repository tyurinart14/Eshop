# Generated by Django 4.0.6 on 2022-09-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='return_status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]