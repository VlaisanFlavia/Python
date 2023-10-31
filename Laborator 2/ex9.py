def find_seats(matrix):
    seats = []

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            current_height = matrix[row][col]

            for r in range(row - 1, -1, -1):
                if matrix[r][col] >= current_height:
                    seats.append((row, col))
                    break

    return seats


# Example usage:
matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = find_seats(matrix)
print(result)
