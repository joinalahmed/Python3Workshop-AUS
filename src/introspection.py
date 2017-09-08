import inspect


def example():
    """
    nothing example function.
    :return:
    """
    pass


print(example.__name__)
print(example.__doc__)
print(inspect.getdoc(example))

print((lambda: None).__name__)
