import random

secret_number = random.randint(1, 100)

attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try Again.")
    elif guess > secret_number:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You guessed correctly.")
        print("Number of attempts:", attempts)
        break
