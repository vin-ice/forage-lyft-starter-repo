from engine.engine import Engine


class SternmanEngine(Engine):
    """concrete Engine class"""
    def __init__(self, warning_light_is_on):
        self.warning_light_on: bool = warning_light_is_on

    def needs_service(self):
        return self.warning_light_on
