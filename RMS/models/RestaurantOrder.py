from ContactData import ContactData
from RestaurantMenuEntry import RestaurantMenuEntry
from typing import Dict
from decimal import Decimal
import datetime

class RestaurantOrder:
    customer_contact_data = ContactData
    menu_selection = Dict[RestaurantMenuEntry, int]
    date = datetime


    def __init__(self, customer_contact_data, menu_selection):
        self.customer_contact_data = customer_contact_data
        self.menu_selection = menu_selection

    def add_or_update_menu_entry(self, menu_entry, count):
        if count > 0:
            self.menu_selection[menu_entry] = count

    def remove_menu_entry(self, menu_entry):
        if menu_entry in self.menu_selection:
            del self.menu_selection[menu_entry]

    def get_cumulative_price(self):
        total_price = Decimal(0)
        for menu_entry, count in self.menu_selection.items():
            total_price += menu_entry.price * count
        return total_price


