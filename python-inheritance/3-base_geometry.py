class BaseGeometry:
    pass

def is_same_attributes(obj):
    expected_attributes = []
    obj_attributes = dir(obj)
    return obj_attributes == expected_attributes
   
bg = BaseGeometry()
print(bg)


print(dir(bg))

print(dir(BaseGeometry))


