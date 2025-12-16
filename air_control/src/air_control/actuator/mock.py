import logging

from air_control.actuator.base import BaseActuator
from air_control.actuator.enum import Position


class MockActuator(BaseActuator):

    def __init__(self, pin, logger: logging.Logger):
        super().__init__(pin, logger)

        self.logger.warning(f"MOCK - Creating actuator on pin {pin}")

    def _motor_move(self, to_position: Position):
        self.logger.info(f"Mock moving to {to_position}")
