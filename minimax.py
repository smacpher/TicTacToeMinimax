import copy

from utils import get_pretty_game_state


def no_more_moves(game_state):
    """Checks if there are any possible moves left"""
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
    if no_more_moves(game_state) or check_win(game_state, 'X') or check_win(game_state, 'O'):  # TODO: optimize me
        return True
    else:
        return False


def check_win(game_state, player):  # TODO: should just return if a win is found; leave get_score to deal with who's turn it is
    rows, cols = len(game_state), len(game_state[0])
    for row in range(rows):
        for col in range(cols):
            start_row = row
            start_col = col
            if check_win_from_cell(game_state,
                                   start_row,
                                   start_col,
                                   player):
                return True
    return False


def check_win_from_cell(game_state, start_row, start_col, player):
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
                if (check_win_from_cell_in_dir(game_state,
                                               start_row,
                                               start_col,
                                               d_row,
                                               d_col,
                                               player)):
                    return True
    return False


def check_win_from_cell_in_dir(game_state, start_row, start_col, d_row, d_col, player):
    win_length = len(game_state)
    for i in range(win_length):
        row = start_row + i * d_row
        col = start_col + i * d_col
        if game_state[row][col] != player:
            return False
    return True


def get_score(game_state, max_player):  # player as of now can be 'X' or 'O'
    player = 'X' if max_player else 'O'
    score = 10 if max_player else -10
    if check_win(game_state, player):
        return score
    else:  # no one wins
        return 0


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


def get_possible_states(state, player):  # pass in a player of 'X' or 'O'
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


def get_player(max_player):
    if max_player:
        return 'X'
    else:
        return 'O'

def minimax_wrapper(state, max_player, depth):

    choice = {'choice': None}  # no nonlocal in python2.7; this is a workaround

    def minimax(state, max_player, depth):
        if is_end_state(state) or depth == 0:  # base case
            score = get_score(state, not max_player)  # get_score with previous player
            return score
        else:
            states = []  # TODO (smacpher): change this to moves; implement a state_to_move function
            scores = []
            # populate moves and scores
            player = get_player(max_player)
            for child_state in get_possible_states(state, player):
                score = minimax(child_state, not max_player, depth-1)
                scores.append(score)
                states.append(child_state)

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


_state = [['X', 'X', 'O'],
          ['O', None, None],
          [None, None, None]]

print(get_pretty_game_state(_state))

choice = minimax_wrapper(_state, True, depth=10)

print(choice)
print(get_pretty_game_state(choice))

state2 = [['X', 'X', 'O'],
          ['O', 'X', None],
          [None,'O', None]]

choice2 = minimax_wrapper(state2, True, depth=10)

print(get_pretty_game_state(choice2))
# TODO: rewrite check win function; it is definitely broken