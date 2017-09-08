class Borg:
    _namespace = {}

    def __init__(self):
        self.__dict__ = Borg._namespace


b1 = Borg()
setattr(b1, 'Hello', 'Hi')
print(b1.Hello)
b2 = Borg()
print(b2.Hello)
setattr(b2, 'Hello', 'Bye')
print(b1.Hello)
