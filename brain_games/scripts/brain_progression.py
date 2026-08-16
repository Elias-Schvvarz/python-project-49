from brain_games.engines.run_game_module import run_game
from brain_games.games.play_progression_module import play_progression

GAME_RULE = 'What number is missing in the progression?'


def main():
    run_game(
        rule=GAME_RULE,
        game_logic=play_progression,
    )


if __name__ == "__main__":
    main()