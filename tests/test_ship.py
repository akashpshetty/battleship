from unittest import TestCase
from ship import AircraftCarrier


class ShipTest(TestCase):
    def test_player_should_be_able_create_an_aircraft_carrier(self):
        AircraftCarrier()

    def test_ac_size_should_be_5(self):
        ac = AircraftCarrier()
        self.assertEqual(ac.size, 5)

    def test_ship_size_should_be_immutable(self):
        ac = AircraftCarrier()
        with self.assertRaises(Exception):
            ac.size = 10
