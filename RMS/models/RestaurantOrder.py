from .ContactData import ContactData
from .RestaurantMenuEntry import RestaurantMenuEntry
from decimal import Decimal
from django.db import models


class RestaurantOrder(models.Model):
    customer_contact_data = models.ForeignKey(ContactData, on_delete=models.CASCADE)
    menu_selection = models.ManyToManyField(RestaurantMenuEntry, through='MenuSelection', null=True)
    date = models.DateTimeField()

    def add_or_update_menu_entry(self, menu_entry, count):
        if count > 0:
            menu_selection, created = MenuSelection.objects.get_or_create(order=self, menu_entry=menu_entry)
            menu_selection.count = count
            menu_selection.save()

    def remove_menu_entry(self, menu_entry):
        menu_selection = MenuSelection.objects.get(order=self, menu_entry=menu_entry)
        menu_selection.delete()

    def get_cumulative_price(self):
        total_price = Decimal(0)
        menu_selections = MenuSelection.objects.filter(order=self)
        for menu_selection in menu_selections:
            total_price += menu_selection.menu_entry.price * menu_selection.count
        return total_price


class MenuSelection(models.Model):
    order = models.ForeignKey(RestaurantOrder, on_delete=models.CASCADE)
    menu_entry = models.ForeignKey(RestaurantMenuEntry, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()
