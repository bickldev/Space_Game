import random
from anomaly import Anomaly
from battle import Battle
from ship import Ship
from events import Events
from trader import Trader


class System:
    system_type = "S"
    current_ship : Ship

    def set_ship(self, current_ship: Ship):
        self.current_ship = current_ship
        # Calls an event
        if self.current_ship.get_location() != [0,0]:
            # 50/50 whether an event occurs
            if random.randint(0, 1):
                self.event = self.random_event()
                
                match self.event:
                    case "Anomaly":
                        self.current_event = Anomaly(self.event)
                    case "Battle":
                        self.current_event = Battle(self.event)
                    case "Trader":
                        self.current_event = Trader(self.event)

    def get_ship(self):
        self.current_ship = None

    def random_event(self):
        choices = ["Anomaly", "Battle", "Trader"]
        return random.choice(choices)