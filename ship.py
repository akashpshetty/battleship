class ShipSize():
    def __init__(self, init_value, name="Ship"):
        self.val = init_value
        self.name = name

    def __get__(self, obj, cls):
        return self.val if obj else self

    def __set__(self, obj, value):
        raise AttributeError("can't set attribute")


class Ship:
    """
        This is the base class for all the ships in this game
    """


class AircraftCarrier(Ship):
    """
        This is the Aircraft carrier
    """
    size = ShipSize(5)


class BattleShip(Ship):
    """
        This is the Battleship
    """
    size = ShipSize(4)


class Submarine(Ship):
    """
        This is the Submarine
    """
    size = ShipSize(3)


class Destroyer(Ship):
    """
        This is the Destroyer
    """
    size = ShipSize(3)


class PatrolBoat(Ship):
    """
        This is the Patrol Boat
    """
    size = ShipSize(2)
