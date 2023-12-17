'''Importing the Base class from base.py'''
from base import Base
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
    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    '''Getter and setter for height'''
    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    ''' Getter and setter for x'''
    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    ''' Getter and setter for y'''
    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

