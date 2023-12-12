'''the module will introduce new concepts ie getter and setter '''
class Square:

    '''this is the definition of the self inclusive of the size which as of the previous assignment is set to private'''
    def __init__(self, size=0):
        self.size = size

    @property 
    def size(self):
        return self.__size

    '''a new term setter has been introduced and will be used to set the values need to calculate the area os the class Square'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value 

    def area(self):
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Output: Area: 7921 for size: 89

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Output: Area: 9 for size: 3

    try:
        my_square.size = "5 feet"  # This will raise a TypeError
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)  # Output: size must be an integer
print(Square.__dict__)        
