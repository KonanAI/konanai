import pytest
from src.tap.classes.timeframe import Time


def test_time_init_with_seconds():
    # Arrange
    data = 1.0
    unit = "second"

    # Act
    time_obj = Time(data, unit)

    # Assert
    assert time_obj.second == data
    assert time_obj.frame == data * Time.FRAMES_PER_SECOND


def test_time_init_with_frames():
    # Arrange
    data = 100
    unit = "frame"

    # Act
    time_obj = Time(data, unit)

    # Assert
    assert time_obj.second == data / Time.FRAMES_PER_SECOND
    assert time_obj.frame == data


def test_time_init_with_invalid_unit():
    # Arrange
    data = 1.0
    unit = "invalid_unit"

    # Act & Assert
    with pytest.raises(ValueError):
        Time(data, unit)


def test_time_init_with_incorrect_data_type():
    # Arrange
    data = "invalid_data"
    unit = "second"

    # Act & Assert
    with pytest.raises(TypeError):
        Time(data, unit)


def test_addition_of_two_times():
    # Arrange
    time_obj1 = Time(1.0, "second")
    time_obj2 = Time(1.0, "second")

    # Act
    result = time_obj1 + time_obj2

    # Assert
    assert result.second == 2.0


def test_subtraction_of_two_times():
    # Arrange
    time_obj1 = Time(2.0, "second")
    time_obj2 = Time(1.0, "second")

    # Act
    result = time_obj1 - time_obj2

    # Assert
    assert result.second == 1.0


def test_multiplication_with_scalar():
    # Arrange
    time_obj = Time(2.0, "second")
    scalar = 2.0

    # Act
    result = time_obj * scalar

    # Assert
    assert result.second == 4.0


def test_multiplication_with_non_integer_result():
    # Arrange
    time_obj = Time(3.11, "second")
    scalar = 0.5

    # Act & Assert
    with pytest.raises(ValueError):
        time_obj * scalar


def test_division_by_scalar():
    # Arrange
    time_obj = Time(2.0, "second")
    scalar = 2.0

    # Act
    result = time_obj / scalar

    # Assert
    assert result.second == 1.0


def test_division_by_zero():
    # Arrange
    time_obj = Time(2.0, "second")
    scalar = 0.0

    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        time_obj / scalar


def test_division_with_non_integer_result():
    # Arrange
    time_obj = Time(2.0, "second")
    scalar = 1.5

    # Act & Assert
    with pytest.raises(ValueError):
        time_obj / scalar


def test_less_than_operator():
    # Arrange
    time_obj1 = Time(1.0, "second")
    time_obj2 = Time(2.0, "second")

    # Act
    result = time_obj1 < time_obj2

    # Assert
    assert result


def test_less_than_or_equal_operator():
    # Arrange
    time_obj1 = Time(1.0, "second")
    time_obj2 = Time(1.0, "second")

    # Act
    result = time_obj1 <= time_obj2

    # Assert
    assert result


def test_greater_than_operator():
    # Arrange
    time_obj1 = Time(2.0, "second")
    time_obj2 = Time(1.0, "second")

    # Act
    result = time_obj1 > time_obj2

    # Assert
    assert result


def test_greater_than_or_equal_operator():
    # Arrange
    time_obj1 = Time(2.0, "second")
    time_obj2 = Time(2.0, "second")

    # Act
    result = time_obj1 >= time_obj2

    # Assert
    assert result


def test_equality_operator():
    # Arrange
    time_obj1 = Time(2.0, "second")
    time_obj2 = Time(2.0, "second")

    # Act
    result = time_obj1 == time_obj2

    # Assert
    assert result


def test_inequality_operator():
    # Arrange
    time_obj1 = Time(1.0, "second")
    time_obj2 = Time(2.0, "second")

    # Act
    result = time_obj1 != time_obj2

    # Assert
    assert result


def test_second_property():
    # Arrange
    data = 1.0
    unit = "second"
    time_obj = Time(data, unit)

    # Act
    result = time_obj.second

    # Assert
    assert result == data


def test_frame_property():
    # Arrange
    data = 100
    unit = "frame"
    time_obj = Time(data, unit)

    # Act
    result = time_obj.frame

    # Assert
    assert result == data


def test_str_representation():
    # Arrange
    time_obj = Time(1.0, "second")

    # Act
    result = str(time_obj)

    # Assert
    assert result == "Time(second=1.0, frame=100)"


def test_repr_representation():
    # Arrange
    time_obj = Time(1.0, "second")

    # Act
    result = repr(time_obj)

    # Assert
    assert result == "Time(second=1.0, frame=100)"
