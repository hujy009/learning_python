#coding: utf-8
'''
example 1: input radius, calculate the area of a circle
'''

import math

r = float(input("Enter the radius of circle:"))
area = math.pi * r * r

print("The area is :", round(area, 2))