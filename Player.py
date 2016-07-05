import copy
import re

from utils import is_valid_move
from utils import MIN_PLAYER_SYM
from utils import get_pretty_game_state

class Player(object):
    """The human player object."""
    def __init__(self):
        self.symbol = MIN_PLAYER_SYM

    def get_state_from_user_move(self, current_state, move):
        """
        Inputs a tuple, representing the user's move; returns the new state
        with the move applied.
        """
        (row, col) = move
        if is_valid_move(current_state, move):
            temp_state = copy.deepcopy(current_state)
            temp_state[row][col] = MIN_PLAYER_SYM
            return temp_state

    def is_valid_input(self, user_input):
        """Checks the validity of the user's move input."""
        pattern = '\s*\d*\s*\d*\s*'
        return re.search(pattern, user_input)

    def get_user_move(self, current_state):
        """Blocks until player makes a valid move."""
        while True:
            user_input = raw_input('Input your move: ')  # will be in the form [row, col]
            if self.is_valid_input(user_input):
                move_list = user_input.split()
                row, col = int(move_list[0]), int(move_list[1])
                move = (row, col)
                if is_valid_move(current_state, move):
                    return self.get_state_from_user_move(current_state, move)
                else:
                    continue
