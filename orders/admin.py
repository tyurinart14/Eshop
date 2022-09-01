from django.contrib import admin
from orders.models import Orders, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'paid_status',
                    'created', 'updated']
    list_filter = ['paid_status', 'created', 'updated']
    inlines = [OrderItemAdmin]


admin.site.register(Orders, OrderAdmin)
