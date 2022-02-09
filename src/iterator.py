#coding:utf-8

class MyRange:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:       # Mr. Hu: 和一般的range不同
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

print("range(7):", list(range(7)))
print("MyRange(7):", [i for i in MyRange(7)])
print(f"list(MyRange(7)): {list(MyRange(7))}")

print(f"__name__: {__name__}, file: {__file__}")