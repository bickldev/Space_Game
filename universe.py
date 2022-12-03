from ship import Ship
from system import System


class Universe:
    rows = 5
    columns = 6
    current_ship : Ship

    def __init__(self):
        self.universe = [[System() for columns in range(self.columns)] for rows in range(self.rows)]

    def initialize_ship(self):
        self.current_ship = Ship()
        self.universe[0][0].set_ship(self.current_ship)
