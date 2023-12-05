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
      
