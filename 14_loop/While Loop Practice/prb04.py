# Create a Random Number Nummber Guessing Game

import random

number = random.randint(1, 100)
guess = None
tries = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {tries} tries.")

'''
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 63
Congratulations! You guessed the number.\
It took you 3 tries.
'''

# Another Way

import random
number = random.randint(1, 100)
guess = None
tries = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {tries} tries.")
        break

'''
Guess a number between 1 and 100: 50
Too low!
Guess a number between 1 and 100: 75
Too high!
Guess a number between 1 and 100: 63
Congratulations! You guessed the number.
It took you 3 tries.
'''