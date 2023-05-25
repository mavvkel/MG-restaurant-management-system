from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start'),
    path('orders/', views.orders_view, name='orders'),
    path('tables/', views.tables_view, name='tables'),

    path('add_order/', views.add_order_view, name='add-order'),
    path('dish-form/', views.dish_form_view, name='dish-form'),
    path('menu/', views.menu_view, name='menu'),
]