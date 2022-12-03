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

    def move_ship(self):
        current_location = self.current_ship.get_location()
        self.universe[current_location[0]][current_location[1]].get_ship()
        self.universe[1][1].set_ship(self.current_ship)
        self.current_ship.set_location([1,1])
