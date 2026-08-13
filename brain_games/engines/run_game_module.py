from brain_games.cli import get_user_name, get_user_answer_for_string

def welcome_message():
    print("Welcome to the Brain Games!")


def user_lost(user_answer, correct_answer, name):
    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")


def congrats(name):
    print(f'Congratulations, {name}!')


def run_game(rule, game_logic):
    welcome_message()
    name = get_user_name()
    print(rule)
    i = 0
    while i < 3:
        question, correct_answer = game_logic()
        print(question)
        user_answer = get_user_answer_for_string()
        if user_answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            user_lost(correct_answer, user_answer, name)
            return
    congrats(name)

if __name__ == '__main__':
    run_game('','')