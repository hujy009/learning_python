# coding: utf-8

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
    def is_date_valid(date_as_string):
        # mydate = Date.date(date_as_string)
        year, month, day = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2038

d = Date.from_string('2019-11-11')

is_date = Date.is_date_valid('2019-11-11')

print(is_date)