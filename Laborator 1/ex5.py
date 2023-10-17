input_matrix = [
    ["f", "i", "r", "s"],
    ["n", "_", "l", "t"],
    ["o", "b", "a", "_"],
    ["h", "t", "y", "p"]
]


def spiral_order(input_matrix):
    result = ""
    first_line = 0
    last_column = 1
    last_line = 2
    first_column = 2
    second_line = 1
    third_line = 2
    while first_line <= 3:
        result += input_matrix[0][first_line]
        first_line += 1

    while last_column <= 3:
        result += input_matrix[last_column][3]
        last_column += 1

    while last_line >= 0:
        result += input_matrix[3][last_line]
        last_line -= 1

    while first_column >= 1:
        result += input_matrix[first_column][0]
        first_column -= 1

    while second_line <= 2:
        result += input_matrix[1][second_line]
        second_line += 1

    while third_line >= 1:
        result += input_matrix[2][third_line]
        third_line -= 1

    return result


result_string = spiral_order(input_matrix)
print(result_string)
