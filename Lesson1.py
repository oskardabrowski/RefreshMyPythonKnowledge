import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors):")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices


choices = get_choices()


def check_win(player, computer):
    print(f"You chose: {player}, Computer chose: {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == 'scissors':
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == 'scissors':
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "scissors":
        if computer == 'scissors':
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."


dict = {"name": "beau", "color": choices}
