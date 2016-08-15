import copy
import re

from utils import is_valid_move
from utils import get_logger
from utils import MIN_PLAYER_SYM


class Player(object):
    """The human player object."""
    def __init__(self):
        self.logger = get_logger(__name__)
        self.symbol = MIN_PLAYER_SYM

    def get_user_move(self, current_state):
        """Blocks until player makes a valid move."""
        while True:
            user_input = raw_input('Input your move: ')  # will be in the form [row, col]
            if self.is_valid_move_input(user_input):
                move_list = user_input.split()
                row, col = int(move_list[0]), int(move_list[1])
                move = (row, col)
                if is_valid_move(current_state, move):
                    return self.get_state_from_user_move(current_state, move)
            self.logger.info('Please input a valid move.')

    @staticmethod
    def is_valid_move_input(user_input):
        """Checks the validity of the user's move input."""
        pattern = r'\s*\d+\s+\d+\s*'
        return re.search(pattern, user_input)

    @staticmethod
    def get_state_from_user_move(current_state, move):
        """
        Inputs a tuple, representing the user's move; returns the new state
        with the move applied.
        """
        (row, col) = move
        if is_valid_move(current_state, move):
            temp_state = copy.deepcopy(current_state)
            temp_state[row][col] = MIN_PLAYER_SYM
            return temp_state

    def prompt_start(self):
        # prompt user for who goes first.
        first = None
        while first is None:
            user_input = raw_input('Do you want to go first? (y/n)').strip()
            if user_input == 'y':
                first = True
            elif user_input == 'n':
                first = False
            else:
                self.logger.info('Input y or n bruh.')
        return first




