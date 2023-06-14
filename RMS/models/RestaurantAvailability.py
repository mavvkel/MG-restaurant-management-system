from django.db import models


class RestaurantAvailability(models.Model):
    schedule = {}

    def add_or_update_day(self, week_day, start_end_hours):
        self.schedule[week_day] = start_end_hours
        self.schedule = dict(sorted(self.schedule.items()))

    def remove_day(self, week_day):
        if week_day in self.schedule:
            del self.schedule[week_day]

    def __str__(self):
        return_string = '{'
        for day, hours in self.schedule.items():
            return_string += f'{day.label}: {hours}, '
        return_string = return_string[:-2]
        return_string += '}'
        return return_string
