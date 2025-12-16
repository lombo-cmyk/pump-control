import logging


class BaseTemperature:

    def __init__(self, device_id: str, logger: logging.Logger):
        self.device_id = device_id
        self.logger = logger

    def get_temperature(self) -> float:
        return self._read_temperature()

    def _read_temperature(self) -> float:
        raise NotImplementedError
