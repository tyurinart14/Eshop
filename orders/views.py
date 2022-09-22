from django.shortcuts import render
from django.views.generic import DetailView, ListView

from orders.models import OrderItem, Orders
from orders.forms import OrdersCreateForm
from cart.cart import Cart
from products.models import Product


def create_new_order(request):
    user = request.user
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdersCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'], user=user)
                product = item['product']
                product.amount = product.amount - int(item['quantity'])
                product.save()
                user.wallet = user.wallet - item['total_price']
                user.save()

            cart.clean()
            return render(request, 'ready_order.html', {'order': order})
    else:
        form = OrdersCreateForm
    return render(request, 'create_order.html', {'cart': cart, 'form': form})


def orders_user_view(request):
    user_order_items = OrderItem.objects.filter(user=request.user)
    context = {"user_order_items": user_order_items}
    return render(request, "history.html", context)
