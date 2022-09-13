# Generated by Django 4.0.6 on 2022-09-01 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=150)),
                ('paid_status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
                'db_table': 'orders',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='orders.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_items', to='products.product')),
            ],
        ),
    ]