from django.db import models


# TODO: validation of the start_time < end_time so that setters are not needed
class StartEndHours:
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __init__(self, start_time, end_time, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")
        self.start_time = start_time
        self.end_time = end_time

    def set_start_time(self, start_time):
        if start_time >= self.end_time:
            raise ValueError("Start time must be before end time")
        self.start_time = start_time

    def set_end_time(self, end_time):
        if end_time <= self.start_time:
            raise ValueError("End time must be after start time")
        self.end_time = end_time

    def contains_date(self, dt):
        return self.start_time <= dt <= self.end_time

    def __str__(self):
        return f'{self.start_time} to {self.end_time}'
