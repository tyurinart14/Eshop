from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrdersCreateForm
from cart.cart import Cart


def create_new_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrdersCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'], quantity=item['quantity'])
            cart.clean()
            return render(request, 'ready_order.html', {'order': order})
    else:
        form = OrdersCreateForm
    return render(request, 'create_order.html', {'cart': cart, 'form': form})
