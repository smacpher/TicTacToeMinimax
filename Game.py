from configs import DEPTH
from utils import get_logger
from utils import get_pretty_game_state
from utils import is_end_state

class Game(object):
    """Represents a single game"""
    def __init__(self, game_size):
        self.logger = get_logger(__name__)
        self.game_size = game_size
        self._state = None

    @property
    def state(self):
        """Initializes state attribute to an empty game if necessary, then
        returns the state attribute.
        """
        if self._state is None:
            self._state = self.create_new_game()
        return self._state

    def create_new_game(self):
        """
        Initializes a tic-tac-toe board as a 2D-array
        of None values.
        """
        rows = cols = self.game_size
        return [[None] * cols for row in range(rows)]

    def update_state(self, new_state):
        """Updates game state."""
        self._state = new_state

    def loop(self, first, player, ai):
        logger = self.logger
        is_user_turn = first
        while not is_end_state(self.state):
            logger.info(get_pretty_game_state(self.state))
            #  User's turn.
            if is_user_turn: 
                player_state = player.get_user_move(self.state)
                self.update_state(player_state)
            #  AI's turn.
            else:
                ai_state = ai.get_best_state(self.state, True, DEPTH)
                self.update_state(ai_state)
            #  Switch turns.
            is_user_turn = not is_user_turn
        logger.info(get_pretty_game_state(self.state))
        logger.info('GAME OVER.')