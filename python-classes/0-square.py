class Square:
    def __init__(self, size=0):
        self.__size = size if isinstance(size, int) and size >= 0 else 0

    def area(self):
        return self.__size ** 2

my_square_1 = Square()
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square()
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square()
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
