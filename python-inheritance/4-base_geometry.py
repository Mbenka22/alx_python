''' Instantiate the class'''
class BaseGeometry:

    def area(self):
        '''Try calling the area method and catch the raised exception'''
        raise Exception("area() is not implemented")


#bg = BaseGeometry()


# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
