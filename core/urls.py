from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('buy_item/<int:id>', views.buy_item, name='buy_item'),
    path('items/', views.items, name='items'),
    path('items/item/<int:id>', views.item, name='item'),
    path('add_item/', views.add_item, name='add_item'),
    path('items/delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('paypal/', include("paypal.standard.ipn.urls")),
]