from django.db import models
from datetime import datetime


# TODO: validation of the start_time < end_time so that setters are not needed
class StartEndHours(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __init__(self, *args, start_time=None, end_time=None,  **kwargs):
        super().__init__(*args, **kwargs)
        if start_time is not None and end_time is not None:
            if start_time >= end_time:
                raise ValueError("Start time must be before end time")
            self.start_time = start_time
            self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        if start_time >= self.end_time:
            raise ValueError("Start time must be before end time")
        self.start_time = start_time

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        if end_time <= self.start_time:
            raise ValueError("End time must be after start time")
        self.end_time = end_time

    def contains_date(self, dt):
        return self.start_time <= dt <= self.end_time

    def __str__(self):
        return f'{self.start_time} to {self.end_time}'
