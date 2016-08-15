import copy
import logging

from configs import LOGGING_LEVELS
from configs import MAX_PLAYER_SYM
from configs import MAXIMIZING_SCORE
from configs import MIN_PLAYER_SYM
from configs import MINIMIZING_SCORE


def get_player(max_player):
    """Returns a player symbol from the given boolean."""
    if max_player:
        return MAX_PLAYER_SYM
    else:
        return MIN_PLAYER_SYM


def get_logger(name):
    """Gets a logger for the module.  Pass in __name__
    for current module.  LOGGING_LEVELS are defined in configs.py
    """
    for level in LOGGING_LEVELS:
        logging.basicConfig(level=level)
    return logging.getLogger(name)


def get_pretty_game_state(game_state):
    """Outputs a nicely formatted game state"""
    return _prettify_game_state(game_state)


def _prettify_game_state(game_state):
    """Returns a nicely formatted 2-d array for logging purposes"""
    result = ''
    rows = len(game_state)
    for row_index in range(rows):
        row = game_state[row_index]
        result += '\n'
        row_str = map(lambda x: str(x) if x != None else ' ', row)
        result += ' | '.join(row_str)
        result += '\n'
        if row_index < rows - 1:  # don't print on last iteration
            result += '--  --  --'
    return result


def is_valid_move(state, move):
    """
    Returns True if a move (represented by a '(row, col)' tuple) is valid.
    """
    (row, col) = move
    rows, cols = len(state), len(state[0])
    if (row >= rows or row < 0 or
        col >= cols or col < 0 or
        state[row][col] is not None):
        return False
    else:
        return True


def get_possible_states(state, player):
    """Returns an array of all possible game states one move away"""
    rows, cols = len(state), len(state[0])
    possible_game_states = []
    for row in range(rows):
        for col in range(cols):
            if is_valid_move(state, (row, col)):
                temp_state = copy.deepcopy(state)
                temp_state[row][col] = player
                possible_game_states.append(temp_state)
    return possible_game_states


def check_win(game_state, player):
    """Checks if the given player has a winning combo."""
    rows, cols = len(game_state), len(game_state[0])
    for row in range(rows):
        for col in range(cols):
            start_row = row
            start_col = col
            if _check_win_from_cell(game_state,
                                   start_row,
                                   start_col,
                                   player):
                return True
    return False


def _check_win_from_cell(game_state, start_row, start_col, player):
    rows, cols = len(game_state), len(game_state[0])
    one_d_dirs = [-1, 0, +1]
    for d_row in one_d_dirs:
        for d_col in one_d_dirs:
            plausible_end_row = start_row + d_row * (rows - 1)
            plausible_end_col = start_col + d_col * (cols - 1)
            # staying in place
            if d_row == 0 and d_col == 0:
                continue
            # index out of range
            elif (plausible_end_row < 0 or plausible_end_row >= rows or
                          plausible_end_col < 0 or plausible_end_col >= cols):
                continue
            # valid direction
            else:
                if (_check_win_from_cell_in_dir(game_state,
                                               start_row,
                                               start_col,
                                               d_row,
                                               d_col,
                                               player)):
                    return True
    return False


def _check_win_from_cell_in_dir(game_state, start_row, start_col, d_row, d_col, player):
    win_length = len(game_state)
    for i in range(win_length):
        row = start_row + i * d_row
        col = start_col + i * d_col
        if game_state[row][col] != player:
            return False
    return True


def no_more_moves(game_state):
    """Checks if there are any possible moves left."""
    rows, cols = len(game_state), len(game_state[0])
    for row in range(rows):
        for col in range(cols):
            if game_state[row][col] is None:
                return False
    return True


def is_end_state(game_state):
    """Checks if the given state is an end state.  An end state
    is defined as having 1) a winner or 2) no more available moves.
    """
    if no_more_moves(game_state) or check_win(game_state, 'X') or check_win(game_state, 'O'):
        return True
    else:

        return False


def get_score(game_state, max_player):  # TODO : make this cleaner
    """Gets the score of the given state based on the given player."""
    if max_player:
        player, score = MAX_PLAYER_SYM, MAXIMIZING_SCORE
    else:
        player, score = MIN_PLAYER_SYM, MINIMIZING_SCORE

    if check_win(game_state, player):
        return score
    else:  # no one wins
        return 0
