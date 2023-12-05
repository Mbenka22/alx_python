def print_matrix_integer(matrix):
    
 matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 for row in matrix:
        for item in row:
            print("{:d}".format(item), end=" ")
        print()
        