class Ship:
    size_options = ["small", "medium", "large"]
    speed_options = [1, 5, 10]

    def __init__(self):
        self.size = self.size_options[0]
        self.speed = self.speed_options[0]
        self.location = [0,0]

    def move():
        pass

    def fire():
        pass

    def repair():
        pass

    def set_location(self, coordinates):
        self.location = coordinates

    def get_location(self):
        return self.location
