'''Try calling the area method and catch the raised exception'''
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

''' Instantiate the object'''
#bg = BaseGeometry()


# try:
#     print(bg.area())
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
