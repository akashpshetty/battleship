from unittest import TestCase, skip
from board import Board, BoardDimension, BoardPoint
from board import VERTICAL, HORIZONTAL, DIAGONAL
from ship import AircraftCarrier
from board_errors import InvalidDirectionError, InvalidStartPositionError


class BoardTest(TestCase):
    def setUp(self):
        self.b = Board()
        self.battle_ship_dim = BoardDimension(10, 10)

    def test_board_dimension(self):
        self.assertEqual(self.b.dimension, self.battle_ship_dim)

    def test_board_dimension_is_immutable(self):
        new_battle_ship_dim = BoardDimension(15, 16)
        with self.assertRaises(Exception):
            self.b.dimension = new_battle_ship_dim

    def test_board_check_state_on_initialization(self):
        self.assertEqual(self.b.state, "Initialized")

    def test_board_display_after_initilization(self):
        expected_list = (('~' for i in range(self.b.dimension.width))
                         for j in range(self.b.dimension.height))
        zipped_lists = zip(self.b.display(), expected_list)
        for (l1, l2) in zipped_lists:
            self.assertListEqual(list(l1), list(l2))

    def test_board_start_ship_placement(self):
        self.b.start_placement()

    def test_board_check_state_after_start_placement(self):
        self.b.start_placement()
        self.assertEqual(self.b.state, "Configuring")

    def test_placement_of_ship_on_board_vertically(self):
        ac = AircraftCarrier()
        self.b.place_ship(ship=ac, position=BoardPoint(1, 1), direction=VERTICAL)

    def test_placement_of_ship_on_board_horizontally(self):
        ac = AircraftCarrier()
        self.b.place_ship(ship=ac, position=BoardPoint(1, 1), direction=HORIZONTAL)

    def test_placement_of_ship_on_board_diagonally_raises_error(self):
        ac = AircraftCarrier()
        with self.assertRaises(InvalidDirectionError) as ce:
            self.b.place_ship(ship=ac, position=BoardPoint(1, 1),
                              direction=DIAGONAL)

        the_exception = ce.exception
        self.assertEqual(the_exception.error_code, InvalidDirectionError.error_code)

    def test_invalid_ship_placement_outside_board(self):
        ac = AircraftCarrier()
        with self.assertRaises(InvalidStartPositionError) as ce:
            self.b.place_ship(ship=ac, position=BoardPoint(11, 11),
                              direction=VERTICAL)

        the_exception = ce.exception
        self.assertEqual(the_exception.error_code, InvalidStartPositionError.error_code)
