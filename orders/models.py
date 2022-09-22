from django.db import models
from products.models import Product
from user.models import UserModel


class Orders(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=150)
    paid_status = models.BooleanField(default=False)
    order_status = models.CharField(max_length=20, default='in processing')

    class Meta:
        db_table = 'orders'
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        for item in self.items.all():
            return sum(item.get_cost())


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
