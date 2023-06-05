"""Module for the Engine Interface"""
from abc import ABC, abstractmethod


class Engine(ABC):
    @property
    def last_service_mileage(self)-> int:
        """Getter"""
        return self.__last_service_mileage

    @last_service_mileage.setter
    def last_service_mileage(self, mileage):
        self.__last_service_mileage = mileage

    @property
    def current_mileage(self)-> int:
        """Getter"""
        return self.__current_mileage

    @current_mileage.setter
    def current_mileage(self, mileage):
        self.__current_mileage = mileage

    @property
    def warning_light_on(self)-> bool:
        """Getter"""
        return self.__warning_light_on

    @warning_light_on.setter
    def warning_light_on(self, switch):
        self.__warning_light_on = switch
    
    """Engine Interface"""
    @abstractmethod
    def needs_service():
        """Abstract method"""
        pass
