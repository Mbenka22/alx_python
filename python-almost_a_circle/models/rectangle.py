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
# setter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

# setter for height
    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
# setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

# setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Calculate the area of the rectangle using the public method def area(self)

        Returns:
        - int: The area of the rectangle calculated as width * height. the functions from the decorators have been used'''
    
        
        return self.__width * self.__height
#examples
# if __name__ == "__main__":

#     r1 = Rectangle(10, 2)
#     print(r1.id)

#     r2 = Rectangle(2, 10)
#     print(r2.id)

#     r3 = Rectangle(10, 2, 0, 0, 12)
#     print(r3.id)
        
# examples1
# if __name__ == "__main__":

#     try:
#         Rectangle(10, "2")
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         r = Rectangle(10, 2)
#         r.width = -10
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

    # try:
        # r = Rectangle(10, 2)
        # r.x = {}
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))

#     try:
#         Rectangle(10, 2, 3, -1)
#     except Exception as e:
#         print("[{}] {}".format(e.__class__.__name__, e))   

# example2  
# if __name__ == "__main__":

#     r1 = Rectangle(3, 2)
#     print(r1.area())

#     r2 = Rectangle(2, 10)
#     print(r2.area())

#     r3 = Rectangle(8, 7, 0, 0, 12)
#     print(r3.area())

