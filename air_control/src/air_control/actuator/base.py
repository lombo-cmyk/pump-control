import logging

from air_control.actuator.enum import Position


class BaseActuator:
    def __init__(self, pin, logger: logging.Logger):
        self.pin = pin
        self.position = None

        self.logger = logger

    def move_right(self):
        self._move(Position.RIGHT)

    def move_left(self):
        self._move(Position.LEFT)

    def can_move(self, to_position: Position) -> bool:
        if self.position == to_position:
            return False
        return True

    def _move(self, to_position: Position):
        if not self.can_move(to_position):
            self.logger.warning(f"Cannot move to current position - {to_position}")
            return

        self._motor_move(to_position)
        self.position = to_position

    def _motor_move(self, to_position: Position):
        raise NotImplementedError
