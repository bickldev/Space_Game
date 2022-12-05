import random
from ship import Ship
from events import Events


class System:
    system_type = "S"
    current_ship : Ship

    def set_ship(self, current_ship: Ship):
        self.current_ship = current_ship
        # Calls an event
        # if self.current_ship.get_location() != [0,0]:
        #     self.event = Events(self.random_event())

    def get_ship(self):
        self.current_ship = None

    def random_event(self):
        choices = ["Anomaly", "Battle", "Trader"]
        return random.choice(choices)