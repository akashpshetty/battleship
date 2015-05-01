from collections import namedtuple

BoardPoint = namedtuple('Point', 'x y')
BoardDimension = namedtuple('Dimension', 'width height')
VERTICAL, HORIZONTAL = 1, 2

class Board:
    __board_dim = BoardDimension(10, 10)
    __board_states = {0: "Initialized",
                      1: "Configuring",
                      2: "In Progress",
                      3: "Completed"}

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

    def place_ship(self, ship, position, direction):
        pass

    def display(self):
        return (('~' for i in range(self.dimension.width))
                for j in range(self.dimension.height))

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.display())
