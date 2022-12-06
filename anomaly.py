import random
from events import Events

class Anomaly(Events):

    def __init__(self, type_of_event):
        super().__init__(type_of_event)
        print("Anomaly started!")
        self.result = "N/A"

        self.decision = input("Would you like to investigate? Y/N ").capitalize()

        if self.decision == "Y":
            print("Scanning anomaly...")
            self.get_result()
            print(self.result)

    def get_result(self):
        random_value = random.randint(1, 6)

        match random_value:
            case 1:
                self.result = "It was just gas."
            case 2:
                self.result = "This gas is more interesting..."
            case 3:
                self.result = "Spacial rift detected!"
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
