from django.db import models
from django.utils.translation import gettext_lazy as _
from RMS.models.RestaurantAvailability import RestaurantAvailability
from django.core.validators import MinLengthValidator
from django.core.validators import MinValueValidator


class RestaurantWorker(models.Model):
    class RestaurantWorkerRole(models.IntegerChoices):
        WAITER = 1, _('Waiter')
        DISHWASHER = 2, _('Dishwasher')
        CHEF = 3, _('Chef')
        MANAGER = 4, _('Manager')
        CLEANER = 5, _('Cleaner')

    def __init__(self, name, role, availability=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.role = role
        self.availability = availability

    name = models.CharField(max_length=200,
                            validators=[MinLengthValidator(limit_value=2,
                                                           message='Name must be at least 2 characters long.')])
    role = models.IntegerField(choices=RestaurantWorkerRole.choices)

    # Not certain it works like that
    availability = RestaurantAvailability

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability

    def add_table(self, table):
        self.tables.append(table)

    def remove_table(self, table):
        if table in self.tables:
            self.tables.remove(table)

    def get_tables(self):
        return self.tables
