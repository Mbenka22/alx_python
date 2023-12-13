def is_kind_of_class(obj, a_class):
    # Check if the object's class matches the specified class
    if type(obj) is a_class:
        return True
    
    # Check if the object's class inherits from the specified class
    for base_class in type(obj).__bases__:
        if base_class is a_class or is_kind_of_class(base_class, a_class):
            return True
    
    return False
# a = 1
# if is_kind_of_class(a, int):
#     print("{} comes from {}".format(a, int.__name__))
# if is_kind_of_class(a, float):
#     print("{} comes from {}".format(a, float.__name__))
# if is_kind_of_class(a, object):
#     print("{} comes from {}".format(a, object.__name__))
