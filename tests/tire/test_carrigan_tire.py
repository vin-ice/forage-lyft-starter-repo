from tire.carrigan_tire import CarriganTire
from unittest import TestCase


class TestCarriganTire(TestCase):
    def test_carrigan_tire_should_be_serviced(self):
        tires_state = [0, 0.6, 0.6, 0.9]
        tires = CarriganTire(tires_state)
        self.assertTrue(tires.needs_service())

    def test_carrigan_tire_should_not_be_serviced(self):
        tires_state = [0, 0, 0, 0]
        tires = CarriganTire(tires_state)
        self.assertFalse(tires.needs_service())
