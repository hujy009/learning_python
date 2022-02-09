#coding:utf-8

def fibs():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr

import itertools
print(list(itertools.islice(fibs(), 10)))


def Fib(max):
    n, a, b = 0, 0, 1
    while n <= max:
        yield a
        n += 1
        a, b = b, a + b
    raise StopIteration

print(list(itertools.islice(Fib(10), 11)))
print(list(itertools.islice(Fib(10), 0, 5)))
print(list(itertools.islice(Fib(10), 5, 11)))
print(list(itertools.islice(Fib(10), 5, 11)))
# print(list(itertools.islice(Fib(10), 5, 12)))   # raise StopIteration

