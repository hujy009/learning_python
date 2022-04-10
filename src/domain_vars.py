# coding: utf-8


a = 1

def f2():
    return a + 1


def f3():
    a = a + 1      # a on the left of '=' is a local variable
    return a


def f4():
    global a
    a = a + 3      # now a is the global a which is defined in the line 4
    return a


def f5():
    a = 1
    def bar():
        a = a + 1     # a not referenced to 'a = 1'
        return a
    return bar


def f6():
    a = 1
    def bar():
        nonlocal a    # now a referenced to 'a = 1'
        a = a + 1
        return a
    return bar



if __name__ == "__main__":
    print(f2())      #  2

    # print(f3())    # UnboundLocalError: local variable 'a' referenced before assignment

    print(f4())      # 4

    print(f2())      # now is 5 not 2

    # print(f5()())    # UnboundLocalError: local variable 'a' referenced before assignment

    print(f6()())