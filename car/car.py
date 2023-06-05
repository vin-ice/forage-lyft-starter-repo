from abc import ABC, abstractmethod

from engine.engine import Engine
from battery.battery import Battery

class Car(ABC):
    """Car Interface"""
    __engine, __battery = None, None

    @property
    def engine(self) -> Engine:
        """Getter function"""
        return self.__engine

    @engine.setter
    def engine(self, eng: Engine) -> None:
        """Setter"""
        self.__engine = eng

    @property
    def battery(self) -> Battery:
        """Getter function"""
        return self.__battery

    @battery.setter
    def battery(self, batt: Battery) -> None:
        """Setter"""
        self.__battery = batt

    @abstractmethod
    def needs_service(self):
        pass
