from random import choice

# TODO: Determine if the user wins, the cpu wins, or its a draw
def result(user_choice,cpu_choice):
    match_result = ""
    match user_choice:
        case "rock":
            match cpu_choice:
                case "rock":
                    match_result = "Draw"
                case "paper":
                    match_result = "You Lose!"
                case "scissors":
                    match_result = "You Win!"

        case "paper":
            match cpu_choice:
                case "rock":
                    match_result = "You Win!"
                case "paper":
                    match_result = "Draw"
                case "scissors":
                    match_result = "You Lose!"

        case "scissors":
            match cpu_choice:
                case "rock":
                    match_result = "You Lose!"
                case "paper":
                    match_result = "You Win!"
                case "scissors":
                    match_result = "Draw"
    return match_result

# Challenge: TODO: Robust Input
# Challenge: TODO: Multi-rounds
def main():
    playing = input("Want to play rock, paper, scissors?[y/n]: ")
    while playing == "y":
        # Ask the user for an input
        user_choice = input("Pick a choice (rock/paper/scissors): ")

        # Error handling
        if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
            print("Enter a valid choice!")
            break

        # Make a random choice for the computer
        # Note: Read the slide for this part
        options = ["rock", "paper", "scissors"]
        cpu_choice = choice(options)

        # Print result
        print(f"{result(user_choice,cpu_choice)}: Computer choose {cpu_choice}")

        # Ask if user wants to play again
        playing = input("Want to play rock, paper, scissors?[y/n]: ")

    if playing != "y":
        print("Thanks for playing!")

main()