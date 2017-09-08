import random


class Example:
    def __new__(cls, *args, **kwargs):
        cls = random.choice(cls.__subclasses__())
        return super(Example, cls).__new__(cls, *args, **kwargs)


class Spam(Example):
    pass


class Eggs(Example):
    pass


print(Example())
print(Example())
