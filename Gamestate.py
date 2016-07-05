import copy
import logging

from utils import get_logger
from utils import get_player
from utils import min_player_sym


class Gamestate(object):
    """Represents a single game"""
    def __init__(self, game_size, state=None, player=True):
        self.game_size = game_size
        self.state = state or self.create_new_game()
        self.player = None
        self.logger = get_logger(__name__, logging.INFO)
        
    def create_new_game(self):
        """
        Initializes a tic-tac-toe board with all values as a 2D-array
        with all values as None
        """
        rows = cols = self.game_size
        return [[None] * cols for row in range(rows)]

    @staticmethod
    def get_score(game_state, max_player):
        if Gamestate.check_win(game_state, max_player):
            return +10
        elif Gamestate.check_win(game_state, not max_player):
            return -10
        else:  # no one wins
            return 0

    @staticmethod
    def get_possible_moves(state, max_player):
        """Returns an array of all possible game states one move away"""
        player = get_player(max_player)
        rows, cols = len(state), len(state[0])
        possible_game_states = []
        for row in range(rows):
            for col in range(cols):
                if Gamestate.is_valid_move(state, (row, col)):
                    temp_state = copy.deepcopy(state)
                    temp_state[row][col] = player
                    possible_game_states.append(temp_state)
        return possible_game_states

    @staticmethod
    def is_valid_move(state, move):
        """
        Returns True if a move (represented by a row, col tuple) is valid
        """
        (row, col) = move
        rows, cols = len(state), len(state[0])
        if (row >= rows or row < 0 or
                col >= cols or col < 0 or
                state[row][col] is not None):
            return False
        else:
            return True

    @staticmethod
    def no_more_moves(game_state):
        """Checks if there are any possible moves left"""
        rows, cols = len(game_state), len(game_state[0])
        for row in range(rows):
            for col in range(cols):
                if game_state[row][col] is None:
                    return False
        return True

    @staticmethod
    def check_win(game_state, max_player):
        player = get_player(max_player)
        rows, cols = len(game_state), len(game_state[0])
        for row in range(rows):
            for col in range(cols):
                start_row = row
                start_col = col
                if Gamestate.check_win_from_cell(game_state, player,
                                            start_row, start_col):
                    return True
        return False

    @staticmethod
    def check_win_from_cell(game_state, player, start_row, start_col):
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
                    if (Gamestate.check_win_from_cell_in_dir(game_state, player,
                                                        start_row, start_col, d_row, d_col)):
                        return True
        return False

    @staticmethod
    def check_win_from_cell_in_dir(game_state, player,
                                   start_row, start_col, d_row, d_col):
        win_length = len(game_state)
        for i in range(win_length):
            row = start_row + i * d_row
            col = start_col + i * d_col
            if game_state[row][col] != player:
                return False
        return True

    def make_move(self, new_state):
        """Updates game state; TODO: handle player changing in main"""
        self.state = new_state

    def get_state_from_user_move(self, move):
        """
        Inputs a tuple, represented user's move; returns the new state
        """
        (row, col) = move
        curr_state = self.state
        if self.is_valid_move(curr_state, move):
            temp_state = copy.deepcopy(self.state)
            temp_state[row][col] = min_player_sym
        return temp_state




