from abc import abstractmethod, ABC


class Tire(ABC):
    @abstractmethod
    def needs_service():
        pass

