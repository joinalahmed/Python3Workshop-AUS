
import datetime


class CurrentTime:
    def __get__(self, instance, owner):
        print(self)
        print(instance)
        print(owner)
        return datetime.datetime.now()


class Example:
    time = CurrentTime()


print(Example().time)
