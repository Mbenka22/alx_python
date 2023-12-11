class Square:
    def __init__(self, size):
        self.__size = size

# Test cases
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))  # Output: <class '__main__.Square'>
    print(my_square.__dict__)  # Output: {'_Square__size': 3}

    try:
        print(my_square.size)  # Trying to access private attribute directly raises an AttributeError
    except AttributeError as e:
        print(e)  # Output: 'Square' object has no attribute 'size'

    try:
        print(my_square.__size)  # Trying to access private attribute directly raises an AttributeError
    except AttributeError as e:
        print(e)  # Output: 'Square' object has no attribute '__size'
