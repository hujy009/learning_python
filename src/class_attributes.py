# coding: utf-8


class Bar: 
    __slots__ = ("name", "age", "notdefined")
    lang = 'python'

Bar.name = 'Sas'
Bar.age = 40
Bar.grade = 'A'     #  it looks __slots__ constrain instance not class

print(f"lang: {Bar.lang}, name: {Bar.name}, age: {Bar.age}, grade: {Bar.grade}")

b = Bar()
# b.bgrade = 'A'   #  AttributeError: 'Bar' object has no attribute 'bgrade'

print(f"b.age: {b.age}")
# b.age = 19         # AttributeError: 'Bar' object attribute 'age' is read-only

b.notdefined = 'can I be changed'
print(f"b.notdefine: {b.notdefined}")

b.notdefined = 'changed'
print(f"b.notdefine: {b.notdefined}")



#######################################################################################################
def findkv(dict, **kwargs):
    return {k: v for k, v in kwargs.items() if dict.get(k) == v}
class Foo:
    lang = 'python'

print(Foo.__dict__)    
print(findkv(Foo.__dict__, lang='python'))
print(hasattr(Foo, 'lang'))

Foo.lang = 'C++'
Foo.group = 'my room'
print(hasattr(Foo, 'lang'))


f = Foo()
rst = list(map(lambda attr: hasattr(Foo, attr), ['lang', 'group'])) 
print(rst)

def myqst(myclass):       # myclass can pointer to Foo etc
    def doesexist(attr):
        return hasattr(myclass, attr)
    return doesexist

myqst_Foo = myqst(Foo)

rst = list(map(myqst_Foo, ['lang', 'group']))
print(rst)

f.age = 25
f.name = 'SS'
rst = list(map(myqst_Foo, ['lang', 'group', 'age', 'name']))
print(rst)      # [True, True, False, False]


myqst_f = myqst(f)
rst = list(map(myqst_f, ['lang', 'group', 'age', 'name']))
print(rst)      # [True, True, True, True]


