'''Importing the fuction of base from the module models and has an empty __init__ file'''
from models.base import Base
''''creating the class Rectangle which has inherited from Base which has been stored in models.base'''
class Rectangle(Base):
    '''Using the init function to create various private attributes'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''using the super function to access the values of the parent class'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    '''Creating the getters and setters for the various attributes'''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
#examples
# if __name__ == "__main__":

#     r1 = Rectangle(10, 2)
#     print(r1.id)

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)
