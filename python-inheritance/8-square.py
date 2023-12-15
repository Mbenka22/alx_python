'''The module from basegeometry 7 has been imported'''
Rectangle = __import__("7-rectangle").Rectangle
'''The child class "Square" will inherit from BaseGeometry'''

class Square(Rectangle):
    '''initializing size'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size",size)
    
    def __str__(self):
         return "[Square] {}/{}".format(self.__size,self.__size)
    '''to find the area of the Square'''
    def area(self):
        return self.__size **2
    
    def _dir_(self):
        '''Customizing the directory for specifications'''
        return sorted  (['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator'])

# s = Square(13)

# print(s)
# print(s.area())
