"""
Module `timeframe` defines a Time class that represents time in seconds
or frames.

This module provides the following class:
- `Time`: Represents time in seconds (float) or frames (int). It provides
methods for arithmetic operations, comparison, and conversions between
the two units.

Classes:
    Time: A class used to represent time in seconds or frames and perform
various operations.

This module is part of the `tap` package.
"""

from typing import Union


class Time:
    """Represent time in seconds or frames."""

    FRAMES_PER_SECOND: int = 100
    UNIT_TYPE: dict[str, type] = {"second": float, "frame": int}

    def __init__(self, data: Union[int, float], unit: str = "second") -> None:
        """
        Initialize a Time object with a time value and unit.

        :param data: Time value in either seconds (float) or frames (int).
        :param unit: Unit of the time value ('second' or 'frame').
        Default is 'second'.
        :raise ValueError: If an invalid unit is provided.
        :raise TypeError: If an incorrect type for the data is provided.
        """
        self._validate_input(data, unit)

        if unit == "second":
            self._second = data
            self._frame = self._convert_seconds_to_frames(data)
        else:  # unit == "frame"
            self._frame = data
            self._second = self._convert_frames_to_seconds(data)

    def __add__(self, other: "Time") -> "Time":
        """
        Return the result of adding another Time object to this one.

        :param Time other: The other Time object.
        :return: The sum of this Time object and the other one.
        :rtype: Time
        """
        return Time(self._second + other._second, "second")

    def __sub__(self, other: "Time") -> "Time":
        """Return result of subtracting another Time object from this one."""
        return Time(self._second - other._second, "second")

    def __mul__(self, scalar: Union[int, float]) -> "Time":
        """Return the result of multiplying the time by a scalar."""
        frames = self._frame * scalar
        if not frames.is_integer():
            raise ValueError("Resulting frames must be an integer.")
        return Time(int(frames), "frame")

    def __truediv__(self, scalar: Union[int, float]) -> "Time":
        """Return the result of dividing the time by a scalar."""
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        frames = self._frame / scalar
        if not frames.is_integer():
            raise ValueError("Resulting frames must be an integer.")
        return Time(int(frames), "frame")

    def __lt__(self, other: "Time") -> bool:
        """Return True if this time is less than the other time."""
        return self._second < other._second

    def __le__(self, other: "Time") -> bool:
        """Return True if this time is less or equal to the other time."""
        return self._second <= other._second

    def __gt__(self, other: "Time") -> bool:
        """Return True if this time is greater than the other time."""
        return self._second > other._second

    def __ge__(self, other: "Time") -> bool:
        """Return True if this time is greater or equal to other time."""
        return self._second >= other._second

    def __eq__(self, other: "Time") -> bool:
        """Return True if this time is equal to the other time."""
        return self._second == other._second

    def __ne__(self, other: "Time") -> bool:
        """Return True if this time is not equal to the other time."""
        return self._second != other._second

    @property
    def second(self) -> float:
        """
        Get the time value in seconds.

        :return: The time value in seconds.
        :rtype: float
        """
        return self._second

    @property
    def frame(self) -> int:
        """
        Get the time value in frames.

        :return: The time value in frames.
        :rtype: int
        """
        return self._frame

    def _validate_input(self, data: Union[int, float], unit: str) -> None:
        """
        Validate the input data and unit.

        :param data: Time value.
        :param unit: Unit of the time value.
        :raise ValueError: If an invalid unit is provided.
        :raise TypeError: If incorrect type for the data is provided.
        """
        if unit not in self.UNIT_TYPE:
            raise ValueError(
                "Invalid unit. Use 'second' for seconds or 'frame' for frames."
            )
        if not isinstance(data, self.UNIT_TYPE[unit]):
            type_name = self.UNIT_TYPE[unit].__name__
            raise TypeError(
                f"Expected a {type_name} for {unit}, got {type(data).__name__}."
            )

    @classmethod
    def _convert_seconds_to_frames(cls, second: float) -> int:
        """
        Convert seconds to frames.

        :param float second: Time value in seconds.
        :return: Time value in frames.
        :rtype: int
        """
        return round(second * cls.FRAMES_PER_SECOND)

    @classmethod
    def _convert_frames_to_seconds(cls, frame: int) -> float:
        """
        Convert frames to seconds.

        :param int frame: Time value in frames.
        :return: Time value in seconds.
        :rtype: float
        """
        return frame / cls.FRAMES_PER_SECOND

    def __str__(self) -> str:
        """
        Return the string representation of the Time object.

        :return: String representation of the Time object.
        :rtype: str
        """
        return f"Time(second={self._second}, frame={self._frame})"

    def __repr__(self) -> str:
        """
        Return the string representation of the Time object.

        :return: String representation of the Time object.
        :rtype: str
        """
        return self.__str__()
