class Game(object):
    """Represents a single game"""
    def __init__(self, game_size):
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
        Initializes a tic-tac-toe board with all values as a 2D-array
        with all values as None
        """
        rows = cols = self.game_size
        return [[None] * cols for row in range(rows)]

    def update_state(self, new_state):
        """Updates game state."""
        self._state = new_state
