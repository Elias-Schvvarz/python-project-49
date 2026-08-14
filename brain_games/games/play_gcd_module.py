import random

def play_gcd():
    a = random.randint(1,20)
    b = random.randint(1, 20)

    question = f'{a} {b}'

    while b != 0:
        new_a = b
        b = a % b
        a = new_a
    result = a

    correct_answer = str(result)

    return question, correct_answer