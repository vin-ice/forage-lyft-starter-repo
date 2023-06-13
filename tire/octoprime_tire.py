from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tires_state):
        self.tires_state = tires_state

    def needs_service(self):
        return sum(self.tires_state) >= 3

