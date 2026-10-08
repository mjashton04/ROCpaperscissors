#Level #5 Assignment - Rock Paper Scissors
#IS 303 – Hilton
#Create a Python game of Rock Paper Scissors.

import random

#Build and use at least two custom functions:
#• get_player_choice: This function should prompt the player, convert the response to
#lowercase, validate the choice, and return the result
#• determine_winner: This function should compare the two choices and return "win",
#"loss", or "tie".

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
        else:
            return player_choice

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("It's a tie!")
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        return "win"
    else:
        print("Computer wins this round!")
        return "loss"

#Welcome the user to the game. 
print("Welcome to Rock Paper Scissors!")

#Ask them how many rounds they would like to play. Ensure that
#the number they enter is an odd number so there cannot be any ties.
while True:
    rounds = int(input("How many rounds would you like to play? (Please enter an odd number): "))
    if rounds % 2 == 1:
        break
    else:
        print("Invalid input. Please enter an odd number.")

#For the game play, ask the user for their choice and then generate a random choice for the
#computer. (NOTE: Make sure that the user’s choice is valid.) 

count = 0
player_wins = 0
computer_wins = 0
while count < rounds:
    count += 1
    player_choice = get_player_choice() 
# Generate a random choice for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
# If there is a tie, the game does not
#count, and we push to the next one.

#  Keep track of the number of wins and losses for both the
#player and the computer. When the game play is over, determine the overall winner and print the
#results.

    result = determine_winner(player_choice, computer_choice)
    if result == "win":
        player_wins += 1
    elif result == "loss":
        computer_wins += 1
    else:
        count -= 1 

print(f"Final Score - Player: {player_wins}, Computer: {computer_wins}")
if player_wins > computer_wins:
    print("Congratulations! You are the overall winner!")
elif computer_wins > player_wins:
    print("Computer is the overall winner! Better luck next time.")
        
