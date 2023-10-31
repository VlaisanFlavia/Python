def number_appearances(string):
    doc = {}

    for char in string:
        if char in doc:
            doc[char] += 1
        else:
            doc[char] = 1

    return doc


example = "Ana has apples."
result = number_appearances(example)
print(result)
