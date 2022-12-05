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

    def move_ship(self, direction):
        self.current_location = self.current_ship.get_location()
        self.current_location = self.get_new_location(direction)
        
        if ((self.current_location[0] >= 0 and self.current_location[1] >= 0) and 
            (self.current_location[0] < self.rows and self.current_location[1] < self.columns)):

            self.universe[self.current_location[0]][self.current_location[1]].get_ship()
            self.current_ship.set_location(self.current_location)
            self.universe[1][1].set_ship(self.current_ship)
            
        else:
            print("Can't move there!")
    
    def get_new_location(self, direction):
        match direction:
            case "N":
                new_location = [self.current_location[0] - 1, self.current_location[1] + 0]
                return new_location
            case "W":
                new_location = [self.current_location[0] + 0, self.current_location[1] - 1]
                return new_location
            case "E":
                new_location = [self.current_location[0] + 0, self.current_location[1] + 1]
                return new_location
            case "S":
                new_location = [self.current_location[0] + 1, self.current_location[1] + 0]
                return new_location
            case "NW":
                new_location = [self.current_location[0] - 1, self.current_location[1] - 1]
                return new_location
            case "NE":
                new_location = [self.current_location[0] - 1, self.current_location[1] + 1]
                return new_location
            case "SW":
                new_location = [self.current_location[0] + 1, self.current_location[1] - 1]
                return new_location
            case "SE":
                new_location = [self.current_location[0] + 1, self.current_location[1] + 1]
                return new_location

        return [0,0]