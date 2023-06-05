from car.calliope_car import CalliopeCar
from car.glissade_car import GlissadeCar
from car.palindrome_car import PalindromeCar
from car.rorschach_car import RorschachCar
from car.thovex_car import ThovexCar

class CarFactory:
    car_types = {
        'calliope': CalliopeCar,
        'glissade': GlissadeCar,
        'palindrome': PalindromeCar,
        'rorschach': RorschachCar,
        'thovex': ThovexCar
    }

    def create_car(self, car_type, *args, **kwargs):
        if car_type in self.car_types:
            car_class = self.car_types[car_type]
            return car_class(*args, **kwargs)
        else:
            raise ValueError(f"Unsupported car type: {car_type}")