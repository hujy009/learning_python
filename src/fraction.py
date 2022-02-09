#coding:utf-8

class Fraction:
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + "/" + str(self.denom)

    __repr__ = __str__

f = Fraction(2, 3)

print(f)      # ==> 2/3


from fractions import Fraction
m, n = Fraction(1, 6), Fraction(3, 6)
print(m)
print(n)
print(m + n)
