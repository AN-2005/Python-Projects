import random

print("========== Rock Paper Scissors ==========")

choices = ["rock", "paper", "scissors"]

user_choice = input("Choose (rock/paper/scissors): ").lower()

computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a Draw!")

elif (
    (user_choice == "rock" and computer_choice == "scissors") or
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
):
    print("🎉 You Win!")

elif user_choice not in choices:
    print("❌ Invalid Choice! Please choose rock, paper, or scissors.")

else:
    print("💻 Computer Wins!")