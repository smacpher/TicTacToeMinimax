import logging

from Gamestate import Gamestate
from utils import get_logger

logger = get_logger(__name__, logging.DEBUG)

def test_check_win():
    logger.debug('Testing check_win()')
    state = [['X', None, None],
             ['O', 'X', None],
             [None, 'O', 'X']]

    assert (Gamestate.check_win(state) == True)

    state = [[None, 'X', 'O'],
             [None, 'X', None],
             [None, 'O', 'X']]

    assert (Gamestate.check_win(state) == False)

    state = [['X', 'O', None],
             [None, 'X', None],
             [None, 'O', 'X']]

    assert (Gamestate.check_win(state) == True)

    state = [['O', None, 'X'],
             [None, None, 'X'],
             [None, 'O', 'X']]
    assert (Gamestate.check_win(state) == True)
    
    logger.debug('PASSED')

