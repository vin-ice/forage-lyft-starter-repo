#!/usr/bin/python3
"""Test suite for the unit: NubbinBattery"""
from battery.battery import Battery
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
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
