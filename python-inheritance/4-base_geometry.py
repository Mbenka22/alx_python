'''The class base geometry'''
class BaseGeometry:
    '''the function for finding the area'''
    def area(self):
        raise Exception("area() is not implemented")
    
    def _dir_(self):
        """
        Customize the dir() output to specify the order of attributes.

        Returns:
            list: A sorted list of attribute names.
        """
        return sorted (['_class', 'delattr', 'dict', 'dir', 'doc', 'eq', 'format', 'ge', 'getattribute', 'gt', 'hash', 'init', 'le', 'lt', 'module', 'ne', 'new', 'reduce', 'reduce_ex', 'repr', 'setattr', 'sizeof', 'str', 'subclasshook', 'weakref_', 'area'])
