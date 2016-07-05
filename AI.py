from utils import get_player
from utils import get_possible_states
from utils import get_score
from utils import is_end_state
from utils import MAX_PLAYER_SYM


class AI(object):
    """The AI player object."""
    def __init__(self):
        self.symbol = MAX_PLAYER_SYM

    def get_best_state(self, state, max_player, depth):
        """Serves as a wrapper for the core minimax algorithm.  The best move --
        represented as a state -- is stored in choice['choice] since python 2.7 doesn't
        support nonlocal variables.
        """
        choice = {'choice': None}  # no nonlocal in python2.7; this is a workaround

        def minimax(state, max_player, depth):
            if is_end_state(state) or depth == 0:  # base case
                score = get_score(state, not max_player)  # get_score with previous player
                return score
            else:
                states = []
                scores = []
                # populate moves and scores
                player = get_player(max_player)
                for child_state in get_possible_states(state, player):
                    score = minimax(child_state, not max_player, depth - 1)
                    scores.append(score)
                    states.append(child_state)
                #  based on the player, choose the best move
                if max_player:
                    max_score_index = scores.index(max(scores))
                    choice['choice'] = states[max_score_index]
                    return scores[max_score_index]
                else:
                    min_score_index = scores.index(min(scores))
                    choice['choice'] = states[min_score_index]
                    return scores[min_score_index]

        minimax(state, max_player, depth)
        return choice['choice']
