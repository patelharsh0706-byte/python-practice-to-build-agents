## Uses the concept of modular functions. 

choices= ('r', 'p', 's')
import random

def get_user_choice():
      while True:
        user_choice= input("Enter your choice (r, p, s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice! Please choose r, p, or s.")

def display_choices(user_choice, comp_choice):
    print("you chose:" +user_choice)
    print("computer chose:" +comp_choice)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        print("It's a draw!")
    elif user_choice == 'r' and comp_choice == 's' or user_choice == 'p' and comp_choice == 'r' or user_choice == 's' and comp_choice == 'p':
        print("You win! Congrats!")
    else: 
        print("Computer wins! Better luck next time.")

def play_game():
    while True:
        user_choice= get_user_choice()
        comp_choice= random.choice(choices)
        display_choices(user_choice, comp_choice)
        determine_winner(user_choice, comp_choice)
                

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break   


play_game()