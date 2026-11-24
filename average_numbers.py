total = 1
sum = 0
userChoice = 1

for i in range(100):

    if userChoice != -1:

        number = int(input("Enter a new integer: "))

        sum += number

        average = sum / total

        print("The running average is", average)

        userChoice = int(input("Enter -1 to stop: "))

        total += 1
