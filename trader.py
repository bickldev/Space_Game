from events import Events

class Trader(Events):

    def __init__(self, type_of_event):
        super().__init__(type_of_event)
        print("Trade started!")