

class SimpleMetaClass(type):
    def __init__(cls, name, bases, attrs):
        print(name)
        print(cls)
        super(SimpleMetaClass, cls).__init__(name, bases, attrs)


class Example(metaclass=SimpleMetaClass):
    pass

class SubExample(Example):
    pass
