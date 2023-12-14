def is_same_class(obj, a_class):
    return type(obj) == a_class



a = 1
if is_same_class(a, int):
    pass
if is_same_class(a, float):
    pass
if is_same_class(a, object):
    pass


