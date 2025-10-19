
from random import randint
# Generate a random number between 0 and 100

random_number = randint(0, 100)

guess_num = int(input("Guess a number between 0 and 100"))
if random_number == guess_num:
    print("You win!")
else:
    print(f"You lose! The number was {random_number}")

