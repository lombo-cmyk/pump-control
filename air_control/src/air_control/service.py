import logging
import time

import schedule

from air_control.actuator.base import BaseActuator
from air_control.actuator.mock import MockActuator
from air_control.temperature.base import BaseTemperature
from air_control.temperature.device import TemperatureReader
from air_control.temperature.mock import MockTemperature
from air_control.utils.env import config


class Service:

    def __init__(self, name: str, logger: logging.Logger):
        self.name = name
        self.logger = logger
        self.input_actuator = self.get_input_actuator()
        self.output_actuator = self.get_output_actuator()
        self.temp_in_sensor = self.get_temperature_in()
        self.temp_out_sensor = self.get_temperature_out()

    def start(self):
        schedule.every(30).seconds.do(self.set_position_job)
        # schedule.every().hour.do(self.set_position_job)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def set_position_job(self):
        temp_in = self.temp_in_sensor.get_temperature()
        temp_out = self.temp_out_sensor.get_temperature()
        if temp_in > temp_out:
            self.input_actuator.move_left()
            self.output_actuator.move_left()
        else:
            self.input_actuator.move_right()
            self.output_actuator.move_right()

    def get_input_actuator(self) -> BaseActuator:
        return self._get_actuator("INPUT")

    def get_output_actuator(self) -> BaseActuator:
        return self._get_actuator("OUTPUT")

    def get_temperature_in(self) -> BaseTemperature:
        return self._get_temperature("IN")

    def get_temperature_out(self) -> BaseTemperature:
        return self._get_temperature("OUT")

    def _get_actuator(self, where: str) -> BaseActuator:
        dev_pin = config[f"{where}_ACTUATOR_PIN"]
        if config[f"{where}_ACTUATOR"] is True:
            self.logger.error("Real actuator not yet implemented")
            raise NotImplementedError
        return MockActuator(dev_pin, self.logger)

    def _get_temperature(self, where: str) -> BaseTemperature:
        dev_id = config[f"TEMPERATURE_{where}_ID"]
        if config[f"TEMPERATURE_{where}"] is True:
            return TemperatureReader(dev_id, self.logger)
        return MockTemperature(dev_id, self.logger)
