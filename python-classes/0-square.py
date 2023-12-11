'''This module will explore the class square'''
class Square:
    def __init__(self, size):
        self.size = size

        '''this function will be used to define the square '''

    def set_size(self, new_size):
        self.size = new_size
        '''I will use the set function to set the parameters of the square'''

    def get_area(self):
        return self.size ** 2


# Create an instance of the Square class
square = Square()

# Get the area of the square
area = square.get_area()
print("Area of the square:", area)  

