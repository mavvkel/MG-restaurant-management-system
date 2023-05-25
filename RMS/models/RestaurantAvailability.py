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
    schedule = models.JSONField(default={})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def toJson(self):
        return json.dumps(self.schedule)

    # def get_schedule(self):
    #     return self.schedule

    def add_or_update_day(self, week_day, start_end_hours):
        self.schedule[week_day] = start_end_hours

    def remove_day(self, week_day):
        if week_day in self.schedule:
            del self.schedule[week_day]
