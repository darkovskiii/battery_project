from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.items, name='items'),
    path('items/item/<int:id>', views.item, name='item'),
    path('add_item/', views.add_item, name='add_item'),
    path('items/delete_item/<int:id>', views.delete_item, name='delete_item')
]