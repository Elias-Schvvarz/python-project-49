from brain_games.engines.run_game_module import run_game
from brain_games.games.play_even_module import play_even

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(
        rule=GAME_RULES,
        game_logic=play_even
    )


if __name__ == '__main__':
    main()