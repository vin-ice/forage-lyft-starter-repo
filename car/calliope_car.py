from car.car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class CalliopeCar(Car):
    """
    A Car concrete class
        Has a Capulet Engine
        Has a Spindler Batt
    """

    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        super.__init__(current_date, last_service_date, current_mileage, last_service_mileage)
        self.engine = CapuletEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
