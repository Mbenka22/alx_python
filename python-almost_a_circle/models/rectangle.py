'''the start of my new module and class'''
class Base:
    '''the new nb-objects with a value of 0'''
    __nb_objects = 0 
    '''setting the id to public'''
    def __init__(self, id=None):
        '''start of the conditions in the function'''
        if id is not None:
            self.id = id
        else:
            '''the base class with the increament setting'''
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
'''the rectangle class which has inherited from the class base'''           
class Rectangle(Base):
    # __width = width
    # __height = height
    # __x = x
    # __y = y

    def __init__(self ,width,height, x = 0 , y = 0 , id = None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
    '''setting the getter and setters for the variables'''  
    #width
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        self.__width = value  

    '''setting the getter and setter for the variable - height'''
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self , value):
        self.__height = value

    ''''setting the getter and setter for "x"'''    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x == value

    '''setting the getter for "y"'''  
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y (self , value):
        self.__y == value
          

r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)      

