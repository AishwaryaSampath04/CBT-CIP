import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_player1_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        player1_choice = get_player1_choice()
        player2_choice = get_computer_choice()
        print(f"Player 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")
        result = determine_winner(player1_choice, player2_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
