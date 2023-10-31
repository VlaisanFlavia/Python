def process_strings(x=1, strings=[], flag=True):
    result_lists = []

    for s in strings:
        char_list = []
        for char in s:
            ascii_code = ord(char)
            if flag:
                is_divisible = (ascii_code % x == 0)
            else:
                is_divisible = (ascii_code % x != 0)

            if is_divisible:
                char_list.append(char)
        result_lists.append(char_list)

    return result_lists


x = 2
strings = ["test", "hello", "lab002"]
flag = False

result = process_strings(x, strings, flag)
print(result)
