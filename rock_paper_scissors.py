# rock, paper and scissors
import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter Rock, Paper, or Scissors.")

def get_computer_choices():
    return [random.choice(["Rock", "Paper", "Scissors"]) for _ in range(3)]

def determine_winner(user_choice, computer_choices):
    print(f"You chose {user_choice}")

    for i, comp_choice in enumerate(computer_choices, start=1):
        print(f"Computer {i} chose {comp_choice}")

    if all(comp_choice == user_choice for comp_choice in computer_choices):
        print("It's a draw!")
    elif any(comp_choice == user_choice for comp_choice in computer_choices):
        print("You win!")
    else:
        print(f"Computer {i} wins!")

def play_game():
    random.seed()  # Initialize the random number generator

    print("Welcome to Rock, Paper, Scissors!")

    user_choice = get_user_choice()
    computer_choices = get_computer_choices()

    determine_winner(user_choice, computer_choices)

if __name__ == "__main__":
    play_game()