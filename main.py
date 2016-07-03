import logging

from Gamestate import Gamestate
from Play import Play
from utils import get_logger
from utils import get_pretty_game_state

SIZE = 3
DEPTH = 6

def main():
    logger = get_logger(__name__, logging.INFO)
    game = Gamestate(SIZE)
    #logger.info(get_pretty_game_state(game.state))

    state = [[None, 'X', 'O'],
             ['O', 'X', None],
             [None, None, None]]

    logger.info(get_pretty_game_state(state))
    AI = Play()

    score, state = AI.minimax(state, DEPTH, True)
    logger.info(score)
    logger.info(get_pretty_game_state(state))

    # while (not Gamestate.no_more_moves(game.state) and not Gamestate.check_win(game.state, True) and
    #        not Gamestate.check_win(game.state, False)):
    #
    #     AI = Play()
    #
    #     score, state = AI.minimax(game.state, DEPTH, True)
    #
    #     game.make_move(state)
    #
    #     if Gamestate.no_more_moves(game.state) or Gamestate.check_win(game.state, True):
    #         break
    #
    #     logger.info(get_pretty_game_state(game.state))
    #
    #     move = None
    #
    #     while not move:
    #         user_input = raw_input('Input your move (ex. row col): ')
    #         row, col = user_input.split()
    #         move = (int(row), int(col))
    #         logger.info(move)
    #
    #         if Gamestate.is_valid_move(game.state, move):
    #             user_input = move
    #         else:
    #             logger.info('Invalid move. Try again')
    #
    #     next_state = game.get_state_from_user_move(user_input)
    #
    #     game.make_move(next_state)
    #
    #     logger.info(get_pretty_game_state(game.state))
    #
    #     if Gamestate.no_more_moves(game.state) or Gamestate.check_win(game.state, False):
    #         break

if __name__ == '__main__':
    main()



