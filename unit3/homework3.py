from random import randint
# Generate a random number between 0 and 100


tryagain = ("yes")

while tryagain == "yes" or "Yes" or "YES" or "yES" or "YeS" or "yEs" or "YEs":
    # Generate a random number between 0 and 100
   
    low = int(input("Enter the low number of the range: "))
    high = int(input("Enter the high number of the range: "))
    random_number = randint(low, high)

    guess_num = int(input(f"Guess a number between {low} and {high}: "))

    if random_number == guess_num:

        print("You win!")

    else:

        print(f"You lose! The number was {random_number}" )
        tryagain = input("Do you want to try again? (yes/no): ")
