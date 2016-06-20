import logging

from Gamestate import Gamestate
from Play import Play
from utils import get_logger
from utils import get_pretty_game_state

SIZE = 3
DEPTH = 3

def main():
    logger = get_logger(__name__, logging.INFO)
    game = Gamestate(SIZE)
    logger.info(get_pretty_game_state(game.state))

    while (not Gamestate.no_more_moves(game.state) and not Gamestate.check_win(game.state, True) and
           not Gamestate.check_win(game.state, False)):

        AI = Play()

        score, state = AI.minimax(game.state, 5, True)

        game.make_move(state)

        if Gamestate.no_more_moves(game.state) or Gamestate.check_win(game.state, True):
            break

        logger.info(get_pretty_game_state(game.state))

        user_input = None

        while not user_input:
            try:
                row, col = raw_input('Input your move (ex. row col): ').split()
                move = (int(row), int(col))
                logger.info(move)

            except:
                logger.info('Please input move in valid format: <row> <col> ')
                continue

            if Gamestate.is_valid_move(game.state, move):
                user_input = move
            else:
                logger.info('Invalid move. Try again')

        next_state = game.get_state_from_user_move(user_input)

        game.make_move(next_state)

        logger.info(get_pretty_game_state(game.state))

        if Gamestate.no_more_moves(game.state) or Gamestate.check_win(game.state, False):
            break

if __name__ == '__main__':
    main()



