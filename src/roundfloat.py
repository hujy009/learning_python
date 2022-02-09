#coding:utf-8

class RoundFloat:
    def __init__(self, val):
        self.value = round(val, 2)
    
    def __str__(self):    # str：用户友好；repr: 解释器友好
        return "{0:.2f}".format(self.value)
    
    __repr__ = __str__

r = RoundFloat(3.1415926)

print(r)    # Mr.Hu: 调用了__str__

print(type(r))  # Mr. Hu: 自定义的对象类型 <class '__main__.RoundFloat'>