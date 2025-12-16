from w1thermsensor import Sensor, W1ThermSensor

from air_control.temperature.base import BaseTemperature


class TemperatureReader(BaseTemperature):

    def __init__(self, device_id, logger):
        super().__init__(device_id, logger)

        self.device = W1ThermSensor(
            sensor_type=Sensor.DS18B20, sensor_id=self.device_id
        )

    def _read_temperature(self) -> int:
        temp = round(self.device.get_temperature(), 1)
        self.logger.debug(f"Temperature on device {self.device_id}: {temp}°C")
        return temp
