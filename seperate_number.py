sentence = input("Enter a sentence: ")

word = ""

for letter in sentence:
    if letter != " ":
        word += letter
    else:
        print(word)
        word = ""

print(word)
