import logging

max_player_sym = 'X'
min_player_sym = 'O'


def get_player(max_player):
    if max_player:
        return max_player_sym
    else:
        return min_player_sym

def get_logger(name, *levels):
    for level in levels:
        logging.basicConfig(level=level)
    return logging.getLogger(name)


def get_pretty_game_state(game_state):
    """Outputs a nicely formatted game state"""
    return prettify_game_state(game_state)


def prettify_game_state(game_state):
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
