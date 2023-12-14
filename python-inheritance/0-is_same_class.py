def is_same_class(obj, a_class):
    return type(obj) == a_class



a = 1
if is_same_class(a, int):
    print(a, int.__name__)
if is_same_class(a, float):
    print(a, float.__name__)
if is_same_class(a, object):
    print(a, object.__name__)


