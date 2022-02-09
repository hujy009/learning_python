# coding: utf-8

class Book:
    def __init__(self, year):
        if str(year) == "2020":
            self.book = "Python 2020"
        else:
            self.book = "Python latest"

    def book_name(self):
        return self.book
        
        
