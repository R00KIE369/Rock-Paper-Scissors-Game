import random

print("Hey this is Rock Paper Scissors Game, the rules are simple, pick your choice - First to 3 wins!")


def play_game():
    user_score = 0
    computer_score = 0
    winning_score = 3

    while True:
        user_action = input("Enter option (Rock, Paper, Scissors): ").capitalize()
        possible_actions = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(possible_actions)

        if user_action not in possible_actions:
            print("Invalid input. Try again. ")
            continue

        print(f"\nYou chose  {user_action}, computer chose {computer_action}.\n")

        if user_action == computer_action:
            print(f"Both player selected {user_action}. It's a draw")
        elif user_action == "Rock":
            if computer_action == "Scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_action == "Paper":
            if computer_action == "Rock":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_action == "Scissors":
            if computer_action == "Paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1

        print(f"Score => You: {user_score} | Computer: {computer_score} ")

        if user_score == winning_score:
            print(f"Congratulations, you won! ")
            break
        elif computer_score == winning_score:
            print(f"You lost (;v;),computer won ")
            break


while True:
    play_game()
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay != "y":
        print("Thanks for playing")
        break
