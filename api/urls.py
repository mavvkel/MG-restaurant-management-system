from django.urls import path
from . import views
from rest_framework.authtoken import views as rf_views

app_name = 'api'

urlpatterns = [
    path('', views.getData),
    path('restaurant/menu', views.RestaurantMenuEntryListView.as_view(), name='menu_entry_list'),
    path('restaurant/menu/<int:pk>', views.RestaurantMenuEntryDetailView.as_view(), name='menu_entry_detail'),
    # TODO: this v should return 403 for wrong credentials
    path('restaurant/table', views.RestaurantTableListView.as_view(), name='restaurant_table_list'),
    path('restaurant/table/booking', views.RestaurantTableBookingView.as_view(), name='restaurant_table_booking'),
    path('restaurant/table/property', views.RestaurantTablePropertyView.as_view(), name='restaurant_table_property'),
    path('restaurant/worker/login', rf_views.obtain_auth_token, name='worker_login'),
]
