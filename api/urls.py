from django.urls import path
from . import views
from rest_framework.authtoken import views as rf_views

app_name = 'api'

urlpatterns = [
    # path('', views.getData),
    path('restaurant/menu', views.RestaurantMenuEntryListView.as_view(), name='menu_entry_list'),
    path('restaurant/menu/<int:pk>', views.RestaurantMenuEntryDetailView.as_view(), name='menu_entry_detail'),
    # TODO: this v should return 403 for wrong credentials
    path('restaurant/worker/login', rf_views.obtain_auth_token, name='worker_login'),
    path('restaurant/worker', views.RestaurantWorkerListView.as_view(), name='worker_entry_list'),
    path('restaurant/worker/<int:pk>', views.RestaurantWorkerListView.as_view(), name='worker_entry_detail'),
    path('restaurant/table', views.RestaurantWorkerListView.as_view(), name='table_list'),
    path('restaurant/table/<int:pk>', views.RestaurantWorkerListView.as_view(), name='table_detail'),
    path('restaurant/deliver_order', views.RestaurantDeliveryRestaurantOrderView.as_view(), name='delivery_list'),
    path('restaurant/deliver_order/<int:pk>', views.RestaurantDeliveryRestaurantOrderDetailView.as_view(),
         name='delivery_detail'),
    path('restaurant/stationary_order', views.StationaryRestaurantOrderView.as_view(),
         name='stationary_order_list'),
    path('restaurant/stationary_order/<int:pk>', views.StationaryRestaurantDetailOrderView.as_view(),
         name='stationary_order_list'),
    path('restaurant', views.RestaurantView.as_view(), name='restaurant'),
]
