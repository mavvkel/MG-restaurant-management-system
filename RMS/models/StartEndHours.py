from django.db import models


class StartEndHours(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __init__(self, start_time, end_time, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        self.save()

    def get_end_time(self):
        return self.end_time

    def set_end_time(self, end_time):
        if end_time <= self.start_time:
            raise ValueError("End time must be after start time")
        self.end_time = end_time
        self.save()

    def contains_date(self, dt):
        return self.start_time <= dt <= self.end_time

