from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tires_state):
        self.tires_state = tires_state

    def needs_service(self):
        for st in self.tires_state:
            if st >= .9:
                return True
        return False

