# coding: utf-8

def foo(arg1, arg2, *args, **kwargs):
    print(f"arg1 is {arg1}")
    print(f"arg2 is {arg2}")
    

    print(f"\nargs: {args}")
    for arg in args:
        print(f"  additional arg: {arg}")

    print(f"\nkwargs: {kwargs}")
    for kw in kwargs:
        print(f"  additioinal kwargs[{kw}]: {kwargs[kw]}")


if __name__ == '__main__':
    print("(1) using listing all arguments individually")
    print("   running: foo('wolf', 3, 'projects', freud=90, gamble=96) ")
    foo('wolf', 3, 'projects', freud=90, gamble=96)    

    print("\n(2) put the non-keyword args in a tuple and the keyword arg in a dic with * and **")
    print("   running: foo(10, 20, *(6, 8), **{'foo': 50, 'bar': 60}) ")
    foo(10, 20, *(6, 8), **{'foo': 50, 'bar': 60})

    print("\n(2.1): but without * or ** ")
    print("   running: foo(10, 20, (6, 8), {'foo': 50, 'bar': 60}) ")
    foo(10, 20, (6, 8), {'foo': 50, 'bar': 60})    