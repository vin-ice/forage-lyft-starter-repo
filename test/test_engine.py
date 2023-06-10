"""Test module for the unit: Engine"""
from engine.capulet_engine import CapuletEngine
from engine.engine import Engine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine 
from unittest.case import TestCase


class TestCapuletEngine(TestCase):
    """Test case for the CapuletEngine engine"""

    def test_capulet_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertIsInstance(engine, Engine)
        self.assertTrue(engine.needs_service())

    def test_capulet_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertIsInstance(engine, Engine)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(TestCase):
    """Test case for the SternmanEngine engine"""

    def test_sternman_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_should_not_be_serviced(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertIsInstance(engine, Engine)
        self.assertFalse(engine.needs_service())


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
