word = input("Enter a string: ")

position = 0

for letter in word:
    if position % 2 == 0:
        print(letter)

    position += 1
