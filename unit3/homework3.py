from random import randint

low = int(input("What do you want your lower number for the range to be? "))
high = int(input("What do you want your higher number for the range to be? "))

random_number = randint(low, high)

max_trials = 3
print(f"You will get {max_trials} tries")

while max_trials > 0:
    guess = int(input("Guess the number between your range: "))
    if guess == random_number:
        print("Congratulations! You have won!")
        break
    else:
        if guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        max_trials -= 1
        if max_trials > 0:
            print("Sorry, not the right number! Try again.")
            print(f"You have {max_trials} tries left.")
        else:
            print("Sorry, you are out of tries. The number was", random_number)

print("game over")
