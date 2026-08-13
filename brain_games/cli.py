import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

if __name__ == '__main__':
    get_user_name()


def get_user_answer_for_string() -> str:
    user_answer = prompt.string('Your answer: ').lower()
    return user_answer
