from datetime import datetime

from car.car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class RorschachCar(Car):
    """
    A Car concrete class
        Has a Willoughby Engine
        Has a Nubbin Batt
    """
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage) -> None:
        super().__init__(current_date, last_service_date, current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date, current_date)
        self.engine = WilloughbyEngine(last_service_mileage, current_mileage)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
