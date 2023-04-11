from RMS.models.ContactData import ContactData
from RMS.models.DishRestaurantMenuEntry import DishRestaurantMenuEntry
from RMS.models.DrinkRestaurantMenuEntry import DrinkRestaurantMenuEntry
from django.contrib import admin


@admin.register(DishRestaurantMenuEntry)
class AdminDishRestaurantMenuEntry(admin.ModelAdmin):
    model = DishRestaurantMenuEntry


@admin.register(DrinkRestaurantMenuEntry)
class AdminDrinkRestaurantMenuEntry(admin.ModelAdmin):
    model = DrinkRestaurantMenuEntry


@admin.register(ContactData)
class AdminContactData(admin.ModelAdmin):
    model = ContactData
