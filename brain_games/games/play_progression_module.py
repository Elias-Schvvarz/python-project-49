import random


def play_progression():
    start_int = random.randint(1, 30)
    index = random.randint(2, 5)
    length = random.randint(8, 12)
    progression = []
    for i in range(length):
        progression.append(str(start_int + i * index))
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    raw_question = ' '.join(progression)
    question = f'Question:{raw_question}'
    return question, correct_answer




