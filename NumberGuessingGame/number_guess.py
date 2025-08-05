import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
            break

guess_number()
