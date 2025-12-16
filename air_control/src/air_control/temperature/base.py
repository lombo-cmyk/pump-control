import logging


class BaseTemperature:

    def __init__(self, pin: int, logger: logging.Logger):
        self.pin = pin
        self.logger = logger

    def get_temperature(self) -> float:
        return self._read_temperature()

    def _read_temperature(self) -> float:
        raise NotImplementedError
