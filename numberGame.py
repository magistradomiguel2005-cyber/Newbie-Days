import random 

def checker(a):
    if a % 2 == 0:
        return True
    else:
        return False

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

attempt = 0

print("Welcome to the number game! I have selected a number between 1 and 10. Can you guess what it is?")
att = int(input("Enter your guess: "))

for i in range(1, 4):
    if att == int(random.choice(numbers)):
        print("Congratulations! You guessed the correct number!")
        break
    else:
        print("Sorry, that's not the correct number. Try again.")
        print("type 1 if you want a hint")
        att = int(input("Enter your answer: "))

        if att == 1:
            if checker(int(random.choice(numbers))):
                print("The number is even.")
            else:
                print("The number is odd.")

        attempt += 1
