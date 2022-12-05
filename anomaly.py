from events import Events

class Anomaly(Events):

    def __init__(self, type_of_event):
        super().__init__(type_of_event)
        print("Anomaly started!")

