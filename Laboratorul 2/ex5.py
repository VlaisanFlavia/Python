def replace(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            if i > j:
                matrix[i][j] = 0

    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = replace(matrix)
print(new_matrix)