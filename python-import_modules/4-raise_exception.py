def raise_exception():
    raise TypeError("This is a type error!")
try:
    raise_exception()
except TypeError as te:
    print("Exception raised")