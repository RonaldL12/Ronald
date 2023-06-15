#imports a library called random that generates a random number
import random 

#forever loops the code 
while True: 
#Definitions 
    player_action = input("Enter a choice (rock, paper, scissors): ")
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")

#List all Condition statements possible = the outcome of the inputs 
#elif is else if 
#Print shows the words in the terminal
#player_action is the local variable 
#computer_action is the global variable 
    if player_action == computer_action:
        print("Both players selected {player_action}. No one wins!")
#Ties if player action = computer action
    elif player_action == "scissors":
        if computer_action == "paper":
            print("Scissors slices paper! Easy dub!")
        else:
            print("Rock destroys scissors! You suck.")
    elif player_action == "rock":
        if computer_action == "scissors":
            print("Rock destroys scissors! Easy dub!")
        else:
            print("Paper wraps rock! You suck.")
    elif player_action == "paper":
        if computer_action == "rock":
            print("Paper wraps rock! Easy dub!")
        else:
            print("Scissors slices paper! You suck.")


