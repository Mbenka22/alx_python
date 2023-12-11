class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

# Example usage:
my_square = Square(3)
print("Size of the square:", my_square.get_size())  # Output: Size of the square: 

my_square.set_size(3)
print("Updated size of the square:", my_square.get_size())  # Output: Updated size of the square: 
