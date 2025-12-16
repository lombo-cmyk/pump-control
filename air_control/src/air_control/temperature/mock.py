from random import uniform

from air_control.temperature.base import BaseTemperature


class MockTemperature(BaseTemperature):

    def __init__(self, device_id, logger):
        super().__init__(device_id, logger)

        self.logger.warning(f"MOCK - Creating temperature sensor {device_id}")

    def _read_temperature(self) -> float:
        temp = round(uniform(-20, 30), 1)
        self.logger.info(
            f"MOCK temperature read on device {self.device_id} to {temp}°C"
        )
        return temp
