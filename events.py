class Events:
    # choices = ["Anomaly", "Battle", "Trader"]

    def __init__(self, type_of_event):
        self.type_of_event = type_of_event
        print("Event!",self.type_of_event)
    
