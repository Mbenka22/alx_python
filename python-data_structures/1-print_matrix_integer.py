def print_matrix_integer(matrix):
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()

# Test the function with the provided matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
