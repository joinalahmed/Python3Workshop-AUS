
import gc

x = 10
print(id(x))
x = "foo"
print(id(x))
x = None
print(id(x))

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)
del a
print(b)


class DelMe:
    def __del__(self):
        print("I am deleting")


a = DelMe()
del a
gc.collect()
print("After deleting object a")
b = DelMe()
b = None
