# coding: utf-8
"""
Define a date: 
    input: year, month, day
    or string year_month_day
    output month/day, year
"""


class Date(object):
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_as_string):
        year, month, day = map(int, date_as_string.split('-'))     # map !!!
        # mydate = Date(year, month, day)                          # hard code 
        mydate = cls(year, month, day)                               # :  cls is better than using hard code
        return mydate

    @staticmethod
    def is_input_valid(date_as_string):
        # mydate = Date.date(date_as_string)
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2038

    @staticmethod
    def is_date_valid(date):
        year, month, day = date.year, date.month, date.day
        return day <= 31 and month <= 12 and year <= 2038

    def __str__(self):
        return f"{self.month}/{self.day}, {self.year}"

d = Date.from_string('2019-11-11')
print(d)

is_input = Date.is_input_valid('2019-11-11')

print(is_input)

is_date = Date.is_date_valid(d)

print(is_date)
