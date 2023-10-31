def compose(list_note, list_param, start):
    melody = [list_note[start]]
    position = start
    for i in range(len(list_param)):
        position += list_param[i]
        if position >= len(list_note):
            position %= len(list_note)
        melody.append(list_note[position])

    return melody


list_note = ["do", "re", "mi", "fa", "sol"]
list_param = [1, -3, 4, 2]
start = 2

melody = compose(list_note, list_param, start)
print(melody)
