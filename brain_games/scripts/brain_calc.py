from brain_games.engines.run_game_module import run_game
from brain_games.games.play_calc_module import play_calc


GAME_RULE = 'What is the result of the expression?'


def main():
    run_game(
        rule = GAME_RULE,
        game_logic = play_calc,
    )

if __name__ == "__main__":
    main()