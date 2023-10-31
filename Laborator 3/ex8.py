def loop(mapping):
    visited = set()
    result = []
    current_key = mapping.get("start")

    while current_key is not None:
        if current_key in visited:
            break
        visited.add(current_key)
        result.append(current_key)
        current_key = mapping.get(current_key)

    return result


mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)
