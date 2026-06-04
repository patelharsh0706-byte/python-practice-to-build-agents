
choice= ('r', 'p', 's')

##user_choice= input("Enter your choice (r, p, s): ").lower()
while True:

    user_choice= input("Enter your choice (r, p, s): ").lower()
    import random
    comp = random.choice(['r', 'p', 's'])
    if user_choice not in choice:
        print("Invalid choice! Please choose r, p, or s.")
        continue

    if user_choice == comp:
            print("you chose:" +user_choice)
            print("computer chose:" +comp)
            print("It's a draw!")


    elif user_choice == 'r' and comp == 's' or user_choice == 'p' and comp == 'r' or user_choice == 's' and comp == 'p':
            print("You win! Congrats!")
            print("you chose:" +user_choice)
            print("computer chose:" +comp)

    else:
            print("Computer wins! Better luck next time.")
            print("you chose:" +user_choice)
            print("computer chose:" +comp)

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break   
    