import dis


def square(x):
    if not isinstance(x, int):
        print("Error: x is a %s instead of int." % type(x))
    else:
        return x * x


def square2(x):
    if not hasattr(x, '__mul__'):
        print("Error: your object do not support multiplication")
    else:
        return x * x


print(square(10))
print(square2(10.1))
print(square.__module__)

# Disassembling function byte codes #

print(square.__code__.co_code)
print(square.__code__.co_varnames)
print(square.__code__.co_argcount)
print(square.__code__.co_consts)

dis.dis(square.__code__)
