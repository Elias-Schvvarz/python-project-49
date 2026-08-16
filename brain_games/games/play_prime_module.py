import random


def play_prime():
    number = random.randint(1,100)
    question = f'Question: {number}'

    if number < 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    for i in range(2, number - 1):
        if number % i == 0:
            correct_answer = 'no'
            break

    return question, correct_answer