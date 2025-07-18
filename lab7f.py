#!/usr/bin/env python3
# Student ID: iconcon 

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    function attributes: __init__, __str__, __repr__,
                         time_to_sec, format_time,
                         change_time, sum_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for display (e.g., 08:30:00)"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a developer-style string using '.' instead of ':'"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """return the result by using sum_times() method"""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string (still available)"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        sum = sec_to_time(self_sec + t2_sec)
        return sum

    def change_time(self, seconds):
        """Change time by adding or subtracting seconds"""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second 
        return None

    def time_to_sec(self):
        """Convert this time object to total seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check if time object has valid hour/minute/second"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert total seconds since midnight to a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
