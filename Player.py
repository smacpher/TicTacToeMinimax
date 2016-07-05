import copy

from utils import is_valid_move
from utils import MIN_PLAYER_SYM


class Player(object):
    """The human player object."""
    def __init__(self):
        self.symbol = MIN_PLAYER_SYM

    def get_state_from_user_move(self, current_state, move):
        """
        Inputs a tuple, represented user's move; returns the new state
        """
        (row, col) = move
        if is_valid_move(current_state, move):
            temp_state = copy.deepcopy(current_state)
            temp_state[row][col] = MIN_PLAYER_SYM
            return temp_state
