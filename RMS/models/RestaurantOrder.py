from .ContactData import ContactData
from .RestaurantMenuEntry import RestaurantMenuEntry
from decimal import Decimal
from django.db import models


class MenuSelection(models.Model):
    menu_entry_id = models.ForeignKey(RestaurantMenuEntry, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


class RestaurantOrder(models.Model):
    customer_contact_data = models.ForeignKey(ContactData, on_delete=models.CASCADE)
    menu_selection = models.ManyToManyField(MenuSelection, null=True)
    date = models.DateTimeField()

    def add_or_update_menu_entry(self, menu_entry_id, count):
        if count > 0:
            temp, _ = MenuSelection.objects.get_or_create(menu_entry_id=menu_entry_id, count=count)
            self.menu_selection.add(temp)

    def remove_menu_entry(self, menu_entry_id):
        menu_selection = MenuSelection.objects.get(order_id=self, menu_entry_id=menu_entry_id)
        menu_selection.delete()

    def get_cumulative_price(self):
        total_price = Decimal(0)
        menu_selections = MenuSelection.objects.filter(order_id=self)
        for menu_selection in menu_selections:
            total_price += menu_selection.menu_entry_id.price * menu_selection.count
        return total_price



