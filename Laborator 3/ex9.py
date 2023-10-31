def my_function(*args1, **args2):
    args2_values = set(args2.values())

    count = 0

    for arg in args1:
        if arg in args2_values:
            count += 1

    return count


result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
