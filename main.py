from configs import DEPTH

from utils import get_logger
from utils import get_pretty_game_state
from utils import is_end_state

from AI import AI
from Game import Game
from Player import Player


def main():
    logger = get_logger(__name__)
    game = Game(3)

    user = Player()
    ai = AI()

    while not is_end_state(game.state):
        new_state = user.get_user_move(game.state)
        game.update_state(new_state)
        logger.info(get_pretty_game_state(game.state))
        new_state2 = ai.get_best_state(game.state, True, DEPTH)
        game.update_state(new_state2)
        logger.info(get_pretty_game_state(game.state))
    print('GAME OVER.')

if __name__ == '__main__':
    main()



