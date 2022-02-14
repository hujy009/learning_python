# coding:utf-8
"""
calculate the occurence of the alpha
"""


def count_letter(s):
    d = {}
    for letter in s:
        if letter.isalpha():
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
    return d


s = 'Life is short You need python'
d = count_letter(s)
print(d)