import random


def play_even():
    number = random.randint(1,100)
    question = f'Question: {number}'
    correct_answer = "yes" if number % 2 == 0 else "no"
    return question, correct_answer