# coding:utf-8

import random

"""
calculate the ocurrence of the number
"""

lst = []
for i in range(100):
    n = random.randint(1, 10)
    lst.append(n)

d = {}
for n in lst:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

print(d)