import random

def load_questions():
    """Return a list of (prompt, [acceptable_answers]) tuples."""
    return [
        ("What is the capital of France?", ["paris"]),
        ("2 + 2 = ?", ["4", "four"]),
        ("Is Python a programming language? (yes/no)", ["yes", "y"]),
        ("What color do you get mixing red and white?", ["pink"]),
        ("What is the boiling point of water in Celsius?", ["100"]),
        ("Is the Earth flat? (yes/no)", ["no", "n"]),
        ("What is the first letter of the alphabet?", ["a"]),
        ("How many legs does a spider usually have?", ["8", "eight"]),
        ("What gas do plants absorb from the air?", ["carbon dioxide", "co2"]),
    ]

def ask_question(q_tuple, q_number, hp):
    """Ask one question, return (correct: bool, new_hp: int)."""
    prompt, answers = q_tuple
    user = input(f"Question {q_number}. {prompt} ").strip().lower()
    if user in answers:
        hp += 3
        print("\tCorrect. You earned 3 points. Your HP is", hp)
        return True, hp
    else:
        hp -= 3
        print("\tIncorrect. You lost 3 points. Your HP is", hp)
        return False, hp

def play_game():
    """Main game loop: pick random questions until HP out of range or questions exhausted."""
    questions = load_questions()
    random.shuffle(questions)
    hp = 9               # starting HP (game ends if <=0 or >=18)
    q_count = 0

    while 0 < hp < 18 and q_count < len(questions):
        q_count += 1
        q = questions[q_count - 1]
        _, hp = ask_question(q, q_count, hp)

    # final outcome
    if hp <= 0:
        print("Game over — you lost all HP.")
    elif hp >= 18:
        print("You won! You reached max HP.")
    else:
        print("No more questions. Final HP:", hp)

if __name__ == "__main__":
    # start the TBAG quiz game
    play_game()
