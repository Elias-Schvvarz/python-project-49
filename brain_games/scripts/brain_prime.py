from brain_games.engines.run_game_module import run_game
from brain_games.games.play_prime_module import play_prime
from brain_games.scripts.brain_gcd import GAME_RULE

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(
        rule = GAME_RULE,
        game_logic = play_prime,
    )

if __name__ == "__main__":
    main()

