#coding:utf-8

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.n += 1
        if self.n > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b        # self.a + self.b 中的self.a还没有改变成self.b的值
        return fib

fibs = Fibs(10000)
lst = [fibs.__next__() for i in range(20)]
print(f"length of lst: {len(lst)}")
print(lst)