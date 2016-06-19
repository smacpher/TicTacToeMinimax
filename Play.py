import copy
import logging

from Gamestate import Gamestate
from utils import get_logger
from utils import get_pretty_game_state


class Play(object):
    """Provides functions to make AI game moves"""
    def __init__(self):
        self.logger = get_logger(__name__, logging.INFO)

    def minimax(self, state, depth, max_player):
        """minimax algo that outputs next state with best score"""
        if Gamestate.check_win(state, max_player) or depth == 0 or Gamestate.is_end_state(state):
            score = Gamestate.get_score(state, not max_player)  # get score for previous player
            print('SCORE: %s' % score)
            print(state)
            return score
        else:
            if max_player:  # AI's turn
                best_value = None
                best_child_state = None
                for child_state in Gamestate.get_possible_moves(state, max_player):
                    child_state_score = self.minimax(child_state, depth-1, 
                                                     not max_player)
                    if best_value is None or child_state_score > best_value:
                        best_value = child_state_score
                        best_child_state = child_state
                return best_value, best_child_state
            else:
                best_value = None
                best_child_state = None
                for child_state in Gamestate.get_possible_moves(state, max_player):
                    child_state_score = self.minimax(child_state, depth - 1, 
                                                     not max_player)
                    if best_value is None or child_state_score < best_value:
                        best_value = child_state_score
                        best_child_state = child_state
                return best_value, best_child_state

