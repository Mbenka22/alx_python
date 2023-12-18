from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
        - size (int): The size (width/height) of the square.
        - x (int, optional): The x-coordinate of the square's position (default is 0).
        - y (int, optional): The y-coordinate of the square's position (default is 0).
        - id (int, optional): The identifier for the square (default is None, which generates an ID).

        Raises:
        - TypeError: If size, x, y, or id are not integers.
        - ValueError: If size is not greater than 0, or if x or y are negative.
        """
        super().__init__(size, x, y, id)
# example        
# if __name__ == "__main__":

#     s1 = Square(5)
#     print(s1)
#     print(s1.area())
#     s1.display()

#     print("---")

#     s2 = Square(2, 2)
#     print(s2)
#     print(s2.area())
#     s2.display()

#     print("---")

#     s3 = Square(3, 1, 3)
#     print(s3)
#     print(s3.area())
#     s3.display()
