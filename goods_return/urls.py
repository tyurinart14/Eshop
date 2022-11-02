from django.urls import path
from goods_return import views

urlpatterns = [
    path('returns/<int:order_id>', views.create_return, name="create_new_return"),
    path('returns', views.ReturnsView.as_view(), name="returns_list"),
    path('refusal/order/<int:order_id>', views.refusal_to_return, name="refusal_order"),
    path('confirm/order/<int:order_id>', views.return_confirmation, name="confirm_return")
]
