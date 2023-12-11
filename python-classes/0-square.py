class Square:
    def __init__(self, size=0):
        self.__size = size if isinstance(size, int) and size >= 0 else 0

    def area(self):
        return self.__size ** 2

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()  # Instantiating with default size
print(type(my_square_2))
print(my_square_2.__dict__)  # This will show an empty dictionary as size is initialized with 0

try:
    print(my_square_1.size)  # AttributeError as size attribute is private
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)  # AttributeError as __size attribute is private
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")  # TypeError as "3" is not an integer
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)  # Instantiation with negative size defaults to 0
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

