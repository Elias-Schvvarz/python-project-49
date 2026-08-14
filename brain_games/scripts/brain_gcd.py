from brain_games.engines.run_game_module import run_game
from brain_games.games.play_gcd_module import play_gcd


GAME_RULE = "Find the greatest common divisor of given numbers."


def main():
    run_game(
        rule = GAME_RULE,
        game_logic = play_gcd,
    )

if __name__ == "__main__":
    main()