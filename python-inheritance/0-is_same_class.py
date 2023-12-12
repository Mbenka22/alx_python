'''this module will cover the class obj  and the is_same is a child of the class a_class'''
def is_same_class(obj, a_class):
    return type(obj) == a_class

'''the new function is introduced'''
a = 1

if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
