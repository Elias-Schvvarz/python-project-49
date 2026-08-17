import random


def play_calc():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    function = random.choice(['+', '-', '*'])

    if function == '+':
        result = a + b
    elif function == '-':
        result = a - b
    else:
        result = a * b

    question = f'Question: {a}{function}{b}'

    correct_answer = str(result)

    return question, correct_answer