import datetime


class StartEndHours:
    _start_time = datetime
    _end_time = datetime

    def __init__(self, start_time, end_time):
        if start_time >= end_time:
            raise ValueError("Start time must be before end time")
        self._start_time = start_time
        self._end_time = end_time

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, start_time):
        if start_time >= self._end_time:
            raise ValueError("Start time must be before end time")
        self._start_time = start_time

    def get_end_time(self):
        return self._end_time

    def set_end_time(self, end_time):
        if end_time <= self._start_time:
            raise ValueError("End time must be after start time")
        self._end_time = end_time

    def contains_date(self, dt):
        return self._start_time <= dt <= self._end_time

