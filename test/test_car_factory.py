"""Test suite for the unit: CarFactory"""
from car import Car
from car_factory import CarFactory as cf
from datetime import datetime
from unittest import TestCase

class TestCarFactory(TestCase):
    """Test case for the CarFactory unit"""
    current_date = datetime.today()
    last_service_date = current_date.replace(day= current_date.day - 1)
    current_mileage = 200
    last_service_mileage = 0
    warning_light_is_on = False

    def test_car_factory_calliope(self):
        car = cf.create_calliope(self.current_date,
                                 self.last_service_date,
                                 self.current_mileage,
                                 self.last_service_mileage)
        self.assertIsInstance(car, Car)

    def test_car_factory_glissade(self):
        car = cf.create_glissade(self.current_date,
                                 self.last_service_date,
                                 self.current_mileage,
                                 self.last_service_mileage)
        self.assertIsInstance(car, Car)

    def test_car_factory_palindrome(self):
        car = cf.create_palindrome(self.current_date,
                                   self.last_service_date,
                                   self.warning_light_is_on)
        self.assertIsInstance(car, Car)

    def test_car_factory_rorshach(self):
        car = cf.create_rorshach(self.current_date,
                                self.last_service_date,
                                self.current_mileage,
                                self.last_service_mileage)
        self.assertIsInstance(car, Car)

    def test_car_factory_thovex(self):
        car = cf.create_rorshach(self.current_date,
                                 self.last_service_date,
                                 self.current_mileage,
                                 self.last_service_mileage)
        self.assertIsInstance(car, Car)
