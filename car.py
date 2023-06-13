from serviceable import Serviceable

class Car(Serviceable):
    """Car Interface"""
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires_state
    def needs_service(self):
        pass
