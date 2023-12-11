# Define the height of the tree
tree_height = 5

# Loop to create the tree
for i in range(tree_height):
    spaces = " " * (tree_height - i - 1)
    stars = "🎄" * (2 * i + 1)
    print(spaces + stars)

# Trunk of the tree
for _ in range(tree_height // 3):
    trunk_spaces = " " * (tree_height - 1)
    trunk = "🎄"
    print(trunk_spaces + trunk)

#NEW PRACTICE QSTION
    tuple1=(1,2,4,3)
    tuple2=(1,2,3,4)
    print(tuple1<tuple2)

#squared
squared_numbers = [x ** 2 for x in range(5)]
print(squared_numbers)

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'),a.count('b'))    


a.insert(2, -1)
a.append(333)
import random
numlist=[]
for i in range(5):
    numlist.append(random.randrange(1,10))
    for i in numlist:
        print(i)


        #oop
class Person:
    pass  # An empty block

p = Person()
print(p)       