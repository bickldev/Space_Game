from ship import Ship


class System:
    system_type = "S"
    current_ship : Ship
    
    def __init__(self):
        pass

    def set_ship(self, current_ship):
        self.current_ship = current_ship

    def get_ship(self):
        self.current_ship = None
