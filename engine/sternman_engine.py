from engine.engine import Engine


class SternmanEngine(Engine):
    """concrete Engine class"""
    def __init__(self, warning_light_is_on):
        self.warning_light_on: bool = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_on:
            return True
        else:
            return False
