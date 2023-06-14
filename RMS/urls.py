from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start'),
    path('orders/', views.orders_view, name='orders'),
    path('tables/', views.tables_view, name='tables'),
    path('add_order/', views.add_order_view, name='add-order'),
    path('dish-form/', views.dish_form_view, name='dish-form'),
    path('table-form/', views.table_form_view, name='table-form'),
    path('drink-form', views.drink_form_view, name='drink-form'),
    path('menu/', views.menu_view, name='menu'),
    path('workers', views.workers_view, name='workers'),
]