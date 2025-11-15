from random import randint

tbag_questions = [
    ["True/False: Python is a coding language.", ["True", "true"]],
    ["Which of these is a valid Python variable? \n1.  hello\n2. if\n3. 你好", ["1", "hello"]],
    ["What does the print() function do? Use one word.", ["print", "Print"]],
    ["Which symbol is used for addition in Python? ", ["+", "plus"]],
    ["True/False: In Python, 5 + 3 equals 8.", ["True", "true"]],
    ["Which symbol is used to make a comment in Python? ", ["#", "hash"]],
    ["Which keyword is used to create a loop in Python? ", ["for", "while"]]
]

hp = 9
questions_done = [False, False, False, False, False, False, False]
fineshedquestions = 0

def printinstructions():
    """Print the game instructions to the player."""
    print("Welcome to the Trivia Game!")
    print("You will be asked a series of questions based on what you learnt in the begginer year.")
    print("For each correct answer, you gain 1 point.")
    print("For each incorrect answer, you lose 1 health point.")
    print("You start with 9 health points. Try to answer as many questions as you can before your health reaches zero!")
    print("Good luck!\n")
    return

while 0 < hp <18:
    
    if fineshedquestions == 7:
        break
    question_number = randint(0, 6)
    while questions_done[question_number]:
        question_number = randint(0, 6)

    fineshedquestions += 1
    questions_done[question_number] = True
    question = tbag_questions[question_number][0]

    answer = input(question)

    if answer in tbag_questions[question_number][1]:
        hp += 3
        print("You answered correctly and gained 3 health points. Your current health is:", hp, "\n")
    else:
        
        hp -= 3
        print("You answered incorrectly and lost 3 health points. Your current health is:", hp, "\n")


if hp <= 0:
    print("Game Over! you did not remember most of the things from begginer year.")
elif hp < hp < 18:
    print("Good effort! You have completed the Trivia Game with a health of", hp, ". You remembered some things from beginner year.")
else:
    print("congratulations! You have completed the Trivia Game with a health of", hp, ". You really remembered a lot from beginner year!")
