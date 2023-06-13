"""Test module for the unit: Engine"""
from engine.engine import Engine
from engine.sternman_engine import SternmanEngine
from unittest.case import TestCase


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
