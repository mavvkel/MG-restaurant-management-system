from django.db import models
import json
from RMS.models.WeekDay import WeekDay
from RMS.models.StartEndHours import StartEndHours
import datetime
from json import JSONEncoder


def default(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()


class RestaurantAvailability(models.Model):
    _schedule = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def toJson(self):
        return json.dumps(self._schedule, default=str)

    def get_schedule(self):
        return self._schedule

    def add_or_update_day(self, week_day, start_end_hours):
        self._schedule[week_day] = start_end_hours

    def remove_day(self, week_day):
        if week_day in self._schedule:
            del self._schedule[week_day]
