#!/usr/bin/python3
"""Test suite for the unit: SpindlerBattery"""
from battery.battery import Battery
from battery.spindler_battery import SpindlerBattery
from datetime import datetime
from unittest import TestCase


class TestSpindlerBattery(TestCase):
    """Test case for the Spindler battery"""
    def test_spindler_battery_should_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 3, day=current_date.day - 1)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        current_date = datetime.today()
        last_service_date = current_date.replace(year=current_date.year - 2)

        battery = SpindlerBattery(last_service_date, current_date)
        self.assertIsInstance(battery, Battery)
        self.assertFalse(battery.needs_service())
