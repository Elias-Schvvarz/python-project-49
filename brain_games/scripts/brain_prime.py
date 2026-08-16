from brain_games.engines.run_game_module import run_game
from brain_games.games.play_prime_module import play_prime

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(
        rule=GAME_RULE,
        game_logic=play_prime,
    )


if __name__ == "__main__":
    main()

