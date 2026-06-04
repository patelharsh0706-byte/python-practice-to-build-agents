Number= input("Guess the number between 1 to 100: ")
import random
num= random.randint(1,100)

while True:
    if int(Number) < num:
        print("Too Low!! Try again")
        Number= input("Guess the number between 1 to 100: ")

    elif int(Number) > num:
        print("Too High!! Try again")
        Number= input("Guess the number between 1 to 100: ")

    else:
        print("Congratulations!! You guessed it right")
        break

