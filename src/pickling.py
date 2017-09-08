# In The Name Of God

import pickle


class IntoBinary:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "My number is " + str(self.number)


my_object = IntoBinary(10)
print(my_object)
pickled = pickle.dumps(my_object)
print(pickled)
my_object = pickle.loads(pickled)
print(my_object)
