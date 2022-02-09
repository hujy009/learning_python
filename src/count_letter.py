# coding:utf-8
"""
calculate the occurence of the alpha
"""

s = 'Life is short You need python'

d = {}
for letter in s:
    if letter.isalpha():
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

print(d)