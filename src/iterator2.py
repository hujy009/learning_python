# coding: utf-8

def Print(my_iterator):
    while True:
        try:
            print(my_iterator.__next__(), end=' ')
        except StopIteration:
            break

print("(1) using iterable.__iter__()")
d = {'a': 1, 'b': 2, 'c': 3}
d_iterator = d.__iter__()        # convert iterable to iterator object
Print(d_iterator)

print("\n\n(2) using built-in iter()")
Print(iter(d))

print("\n\n(3) __iter__ method is to itself")
g = iter(d)
print(g is g.__iter__().__iter__().__iter__().__iter__())