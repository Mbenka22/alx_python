class BaseGeometry:
    pass
bg = BaseGeometry()
print(bg)
def is_same_attributes(obj):
    expected_attributes = []
    obj_attributes = dir(obj)
    return obj_attributes == expected_attributes
   

print(dir(bg))

print(dir(BaseGeometry))


