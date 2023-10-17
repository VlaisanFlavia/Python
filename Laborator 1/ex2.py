example = input("Textul dorit: ")
number = 0

for i in range(len(example)):
    if example[i] in 'aeiouAEIOU':
        number += 1

print("Numarul de vocale este: ", number)
