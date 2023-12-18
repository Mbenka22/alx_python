from models.rectangle import Rectangle
'''the class Square which has inherited from the Rectabngle class'''
class Square(Rectangle):
    '''instantiating the attributes'''
    def __init__(self, size, x=0, y=0, id=None):
        
        '''Initializes a Square instance.'''

        
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
