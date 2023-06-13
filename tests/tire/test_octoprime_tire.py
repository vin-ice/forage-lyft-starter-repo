#!/usr/bin/python3
from tire.octoprime_tire import OctoprimeTire
from unittest import TestCase


class TestOctoprimeTire(TestCase):
    def test_octoprime_tire_should_be_serviced(self):
        tires_state = [0.6, 0.6, 0.9, 0.9]
        tires = OctoprimeTire(tires_state)
        self.assertTrue(tires.needs_service())

    def test_octoprime_tire_should_not_be_serviced(self):
        tires_state = [0, 0, 0, 0]
        tires = OctoprimeTire(tires_state)
        self.assertFalse(tires.needs_service())

