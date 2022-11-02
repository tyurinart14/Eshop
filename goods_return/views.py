from django.shortcuts import render, redirect
from orders.models import OrderItem
from user.models import UserModel
from goods_return.models import ProductReturn
from django.views.generic import ListView


def create_return(request, order_id):
    order = OrderItem.objects.get(id=order_id)
    product_return = ProductReturn.objects.create(user_id=order.user.pk, product_id=order.pk)
    return render(request, "ready_return.html", {'product_return': product_return})


class ReturnsView(ListView):
    model = ProductReturn
    template_name = 'returns_detail.html'


def refusal_to_return(request, order_id):
    return_order = ProductReturn.objects.get(id=order_id)
    order_status = OrderItem.objects.get(id=return_order.product_id)
    order_status.return_status = False
    order_status.save()

    return_order.delete()

    return redirect("returns_list")


def return_confirmation(request, order_id):
    return_order = ProductReturn.objects.get(id=order_id)
    return_product = return_order.product.product
    return_product.amount += int(return_order.product.quantity)
    return_product.save()

    user = return_order.user
    user.wallet += int(return_order.product.quantity * return_order.product.price)
    user.save()

    order = return_order.product
    order.return_status = True
    order.save()

    return_order.delete()
    return redirect("returns_list")
