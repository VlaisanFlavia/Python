example = input("Stringul este:")

# for i in range(len(example)):
#     if example[i].isupper():
#         for j in range(len(example), i-1):
#             example[:i] = example[:j]
#         example[:i] = "_"
#         example[i].lower()
#
# print(example)

result = ""
for caracter in example:
    if caracter.isupper():
        result += "_" + caracter.lower()
    else:
        result += caracter

if result.startswith("_"):
    result = result[1:]

print(result)
