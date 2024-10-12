def square_matrix_simple(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix[i][j] ** 2

    return result

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_matrix = square_matrix_simple(matrix)

print(new_matrix)
print(matrix)