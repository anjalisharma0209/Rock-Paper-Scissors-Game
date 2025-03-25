import random

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_input not in options:
        print("Invalid choice. Try again.")
        continue
    computer_choice = random.choice(options)

    print(f"\nYou choose: {user_input}")
    print(f"Computer choose: {computer_choice}")

    if user_input==computer_choice:
        print("It's a draw! 😊")

    elif (user_input=="rock" and computer_choice=="scissors") or (user_input=="scissors" and computer_choice=="paper") or (user_input=="paper" and computer_choice=="rock"):
        print("➡️ You Win! 🥳")
    else:
        print("❌ You lose!")
        

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 😊")
        break