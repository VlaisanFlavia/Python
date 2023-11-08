class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = 0
                for k in range(self.cols):
                    dot_product += self.get(i, k) * other.get(k, j)
                result.set(i, j, dot_product)
        return result

    def apply_function(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, func(self.get(i, j)))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Initial Matrix:")
print(matrix)

transposed_matrix = matrix.transpose()
print("\nTransposed Matrix:")
print(transposed_matrix)

new_matrix = Matrix(3, 3)
new_matrix.set(0, 0, 3)
new_matrix.set(0, 1, 7)
new_matrix.set(0, 2, 3)
new_matrix.set(1, 0, 6)
new_matrix.set(1, 1, 5)
new_matrix.set(1, 2, 2)
new_matrix.set(2, 0, 1)
new_matrix.set(2, 1, 0)
new_matrix.set(2, 2, 0)


product = matrix.multiply(new_matrix)
print("\nMatrix Multiplication with New Matrix:")
print(product)

matrix.apply_function(lambda x: x * 2)
print("\nMatrix after Applying Lambda (Multiply by 2):")
print(matrix)
