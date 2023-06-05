from car.car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class PalindromeCar(Car):
    """
    A Car concrete class
        Has a Sternman Engine
        Has a Spindler Batt
    """
    def __init__(self, current_date, last_service_date, warning_light_on):
        self.engine = SternmanEngine(warning_light_on)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
