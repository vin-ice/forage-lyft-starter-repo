"""Test module for the unit: WilloughbyEngine"""
from engine.engine import Engine
from engine.willoughby_engine import WilloughbyEngine 
from unittest.case import TestCase


class TestWilloughbyEngine(TestCase):
    """Test case for the Willoughby Engine"""
    def test_willoughby_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertIsInstance(engine, Engine)
        self.assertFalse(engine.needs_service())
