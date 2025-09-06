
from random import choice

# TODO: Ask the user for an input


# TODO: Make a random choice for the computer
# Note: Read the slide for this part
options=["rock", "paper","scissors"]


# TODO: Determine if the user wins, the cpu wins, or its a draw

playing = input("Want to play rock, paper, scissors?[y/n]: ")


while playing == "y":
    user_choice = input("Pick a choice (rock/paper/scissors): ")
    cpu_choice = choice(options)

    result = ""
    match user_choice:
        case "rock":
            match cpu_choice:
                case "rock":
                    result = "Draw"
                case "paper":
                    result = "You Lose!"
                case "scissors":
                    result = "You Win!"

        case "paper":
            match cpu_choice:
                case "rock":
                    result = "You Win!"
                case "paper":
                    result = "Draw"
                case "scissors":
                    result = "You Lose!"

        case "scissors":
            match cpu_choice:
                case "rock":
                    result = "You Lose!"
                case "paper":
                    result = "You Win!"
                case "scissors":
                    result = "Draw"
        case _:
            print("Enter a valid choice!")


    if result != "":
        print(f"{result}: Computer choose {cpu_choice}")

    playing = input("Want to play rock, paper, scissors?[y/n]: ")

if playing != "y":
    print("Thanks for playing!")
# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds
