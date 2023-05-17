from django.db import models


class RestaurantAvailability:
    def __init__(self):
        self._schedule = {}

    def get_schedule(self):
        return self._schedule

    def add_or_update_day(self, week_day, start_end_hours):
        self._schedule[week_day] = start_end_hours

    def remove_day(self, week_day):
        if week_day in self._schedule:
            del self._schedule[week_day]
