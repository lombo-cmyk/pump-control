from random import randint

from air_control.temperature.base import BaseTemperature


class MockTemperature(BaseTemperature):

    def __init__(self, pin, logger):
        super().__init__(pin, logger)

        self.logger.warning(f"MOCK - Creating temperature sensor on pin {pin}")

    def _read_temperature(self) -> int:
        self.logger.info("Mocking temperature read")
        return randint(-20, 30)
