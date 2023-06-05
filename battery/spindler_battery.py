"""Module for a concrete Battery class"""
from datetime import datetime

from battery.battery import Battery

class SpindlerBattery(Battery):
    """A concrete class for the Battery Interface"""
    last_service_date: datetime
    current_date: datetime

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        """implementation"""
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < self.current_date:
            return True
        else:
            return False
