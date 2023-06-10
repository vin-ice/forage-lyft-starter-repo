"""Test suite for the unit: Battery"""
from battery.battery import Battery
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from unittest import TestCase


class TestNubbinBattery(TestCase):
    """Test case for the Nubbin battery"""

    def test_nubbin_battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 4, day=current_date.day - 1)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertTrue(battery.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = NubbinBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(TestCase):
    """Test case for the Spindler battery"""
    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 2, day=current_date.day - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertFalse(battery.needs_service())
