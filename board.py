from collections import namedtuple
from board_errors import InvalidDirectionError, InvalidStartPositionError

BoardPoint = namedtuple('Point', 'x y')
BoardDimension = namedtuple('Dimension', 'width height')
VERTICAL, HORIZONTAL, DIAGONAL = 1, 2, 3


class Board:
    __board_dim = BoardDimension(10, 10)
    __board_states = {0: "Initialized",
                      1: "Configuring",
                      2: "In Progress",
                      3: "Completed"}
    __valid_directions = (VERTICAL, HORIZONTAL)

    def __init__(self):
        self.__state = self.__board_states[0]

    @property
    def dimension(self):
        return self.__board_dim

    @property
    def state(self):
        return self.__state

    def start_placement(self):
        self.__state = self.__board_states[1]

    def _is_valid_placement(self, ship, position, direction):
        if direction not in self.__valid_directions:
            raise InvalidDirectionError()

        if position.x > self.__board_dim.width or\
            position.y > self.__board_dim.height:
            raise InvalidStartPositionError()

    def place_ship(self, ship, position, direction):
        try:
            self._is_valid_placement(ship, position, direction)
        except:
            raise

    def display(self):
        return (('~' for i in range(self.dimension.width))
                for j in range(self.dimension.height))

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.display())
