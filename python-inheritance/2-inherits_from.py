
def inherits_from(obj, a_class):
    ''' Get the classes the object is an instance of'''
    obj_classes = type(obj).__mro__
    
    ''' Check if any class in the object's method resolution order is a subclass of a_class'''
    for cls in obj_classes:
        if cls is a_class or issubclass(cls, a_class):
            return True
    
    return False

