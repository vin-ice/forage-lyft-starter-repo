"""Module for the Engine Interface"""
from abc import ABC, abstractmethod


class Engine(ABC):
    """Engine Interface"""

    @abstractmethod
    def needs_service():
        """Abstract method"""
        pass
