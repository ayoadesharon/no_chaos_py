word = input("Enter a word: ")

vowel = 0
consonant = 0

for i in word:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel += 1
    else:
        consonant += 1

print("Vowels:", vowel)
print("Consonants:", consonant)
