from unittest import TestCase
from battleship import Board


class BoardTest(TestCase):
    def test_board_dimension(self):
        b = Board()
        battle_ship_dim = (10, 10)
        self.assertEqual(b.dimension, battle_ship_dim)

    def test_board_dimension_is_immutable(self):
        b = Board()
        battle_ship_dim = (15, 16)
        with self.assertRaises(Exception):
            b.dimension = battle_ship_dim
