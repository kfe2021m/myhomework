
import pytest
from dz11.dz import Time

@pytest.mark.parametrize("hours, minutes, seconds, expected_hours, expected_minutes, expected_seconds", [
    (10, 30, 45, 10, 30, 45),  # Valid input values
    (225, 'g', -5, 25, 0, 0),      # Invalid input values
])
def test_input_time( expected_hours, expected_minutes, expected_seconds):
    t = Time()
    # t.h = hours
    # t.m = minutes
    # t.s = seconds
    assert t.h == expected_hours
    assert t.m == expected_minutes
    assert t.s == expected_seconds

def test_str():
    t = Time(10, 30, 45)
    assert str(t) == "10:30:45"

def test_input_time(mocker):
    mocker.patch('builtins.input',return_value = 1)
    t = Time()
    t.input_time()
    assert t.h == 1
    assert t.m == 1
    assert t.s == 1