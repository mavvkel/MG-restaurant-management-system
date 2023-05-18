from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_view, name='start'),
    path('orders/', views.orders_view, name='orders'),

]