class Square :
    '''This is a class square which has a myriad of parameters and functions such as the height , width amd the area
    '''

    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

# Example usage:
# Create a square with size 5
my_square = Square()
print("Area of the square:", my_square.area())  # Output: Area of the square: 25

