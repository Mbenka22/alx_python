"""Module to define a Square class"""

class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

# Example usage:
# Create a square with size 
my_square = Square()
print("Area of the square:", my_square.area())  # Output: Area of the square: 
