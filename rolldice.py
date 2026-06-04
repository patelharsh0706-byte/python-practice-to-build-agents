playing = True
while True:
    Dice= input("Would you like to roll a dice?(y/n):")
    if Dice== "y":
        import random
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        print("You rolled a dice number:" , dice1, "and", dice2)
    elif Dice== "n":
        print("Thank you, see you later!")

    else:
        print("Invalid input, please enter y or n")
    
    break

