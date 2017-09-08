
class Hello:
    def __init__(self):
        print("Hello created")

    def __str__(self):
        return "Hello"

    def __int__(self):
        return 110

    def __add__(self, other):
        return other

    def __radd__(self, other):
        return other


h = Hello()
print(str(h))
print(int(h))
print(h + 10)
print(10 + h)
