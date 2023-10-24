def group_by_rhyme(strings):
    rhyme = []

    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            end1 = strings[i][-2:]
            end2 = strings[j][-2:]
            if end1 == end2:
                rhyme.append((strings[i], strings[j]))

    return rhyme


strings = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(strings)
print(result)
