from brain_games.cli import get_user_name


def welcome_message():
    print("Welcome to the Brain Games!")


def main():
    welcome_message()
    get_user_name()


if __name__ == '__main__':
    main()