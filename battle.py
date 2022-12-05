from events import Events


class Battle(Events):
    
    def __init__(self, type_of_event):
        super().__init__(type_of_event)
        print("Battle started!")
