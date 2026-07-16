import random

print("===== Number Guessing Game =====")

print("I have selected a number between 1 and 100.")
print("Can you guess it?")

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("Congratulations! You guessed the correct number.")
        print("Number of attempts:", attempts)
        break