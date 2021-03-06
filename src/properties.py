

class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def name(self):
        return "%s, %s" % (self.last_name, self.first_name)

    @name.setter
    def name(self, value):
        pass

    @name.deleter
    def name(self):
        del self.last_name
        del self.first_name
