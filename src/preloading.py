
import functools


def main_function(arg1, arg2, arg3):
    print("arg1 : " + str(arg1))
    print("arg2 : " + str(arg2))
    print("arg3 : " + str(arg3))


partial_function = functools.partial(main_function, arg3=10)
partial_function(20, 30)
