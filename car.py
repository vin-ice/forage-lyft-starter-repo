from serviceable import Serviceable

class Car(Serviceable):
    """Car Interface"""
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass