import logging

from utils import check_win
from utils import get_logger
from utils import get_score
from utils import no_more_moves

logger = get_logger('Tests', logging.DEBUG)


def test_check_win():
    logger.debug('Testing check_win() from minimax.py')
    state = [['X', None, None],
             ['O', 'X', None],
             [None, 'O', 'X']]

    assert (check_win(state, 'X') == True)
    state = [[None, 'X', 'O'],
             [None, 'X', None],
             [None, 'O', 'X']]
    assert (check_win(state, 'X') == False)
    state = [['X', 'O', None],
             [None, 'X', None],
             [None, 'O', 'X']]
    assert (check_win(state, 'O') == False)
    state = [['O', None, 'X'],
             [None, None, 'X'],
             [None, 'O', 'X']]
    assert (check_win(state, 'X') == True)
    state = [['X', 'O', None],
             ['X', 'O', None],
             ['X', 'O', 'X']]
    assert (check_win(state, 'X') == True)
    assert (check_win(state, 'O') == True)
    logger.debug('Passed')


def test_is_end_state():
    logger.debug('Testing is_end_state()')
    state = [[None, 'X', 'O'],
             [None, 'X', None],
             [None, 'O', 'X']]
    assert (no_more_moves(state) == False)
    state = [['X', 'X', 'O'],
             ['O', 'O', 'X'],
             ['X', 'O', 'X']]
    assert (no_more_moves(state) == True)
    logger.debug('Passed')


def test_get_score():
    logger.debug('Testing get_score()')
    state = [['X', 'X', 'O'],
             ['O', 'O', 'X'],
             ['X', 'O', 'X']]
    assert (get_score(state, True) == 0)
    assert (get_score(state, False) == 0)
    state = [['X', None, None],
             ['O', 'X', None],
             [None, 'O', 'X']]
    assert (get_score(state, True) == 10)
    state = [[None, 'X', 'O'],
             [None, 'X', None],
             [None, 'O', 'X']]
    assert (get_score(state, True) == 0)
    assert (get_score(state, False) == 0)
    state = [['O', None, 'X'],
             [None, None, 'X'],
             [None, 'O', 'X']]
    assert (get_score(state, True) == 10)
    assert (get_score(state, False) == 0)
    state = [['X', None, 'O'],
             [None, None, 'O'],
             [None, 'X', 'O']]
    assert (get_score(state, True) == 0)
    assert (get_score(state, False) == -10)
    logger.debug('Passed')


def test_all():
    test_check_win()
    test_is_end_state()
    test_get_score()


if __name__ == '__main__':
    test_all()
