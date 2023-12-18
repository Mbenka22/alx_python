'''Importing the Base class from base.py'''
from models.base import Base
def __init__(self, id=None):
        '''start of the conditions in the function'''
        if id is not None:
            self.id = id
'''creating the child class which has inherited from the imported base class'''
class Rectangle(Base):
    '''initializing the attributes of the rectangle class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''using the super function to access the properties of the  class base'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    ''' Getter and setter for width'''
    @property
    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    '''Getter and setter for height'''
    @property
    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    ''' Getter and setter for x'''
    @property
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    ''' Getter and setter for y'''
    @property
    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
