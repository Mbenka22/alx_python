'''this module will cover the class obj  and the is_same is a child of the class a_class'''
def is_same_class(obj, a_class):
    return type(obj) == a_class

'''the new function is introduced'''
a = 1


if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))