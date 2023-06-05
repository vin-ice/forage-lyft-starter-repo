"""Module for the battery interface"""
from abc import ABC, abstractmethod
from datetime import datetime


class Battery(ABC):
    """Battery Interface"""
    @abstractmethod
    def needs_service():
        """Abstract function for concrete class"""
        pass
