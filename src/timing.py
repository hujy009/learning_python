#coding:utf-8
'''
编写一个用于测试函数执行时间的装饰器函数
'''

import time

def timing_func(func):
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        return stop - start
    return wrapper

@timing_func
def test_list_append():
    lst = []
    for i in range(1000000):
        lst.append(i)

@timing_func
def test_list_compre():
    [i for i in range(1000000)]

a = test_list_append()
c = test_list_compre()
print("test list append time:", a)
print("test list comprehension time:", c)
print('append/compre =', round(a/c, 3))