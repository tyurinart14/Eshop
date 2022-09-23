from django.db import models
from orders.models import OrderItem
from user.models import UserModel


class ProductReturn(models.Model):
    product = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'returns'
        ordering = ('-created',)

    def __str__(self):
        return '{}'.format(self.id)

