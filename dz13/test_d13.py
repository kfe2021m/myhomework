import pytest
from dz13.d13 import Time

@pytest.mark.parametrize("time1, time2, expected_sum", [
    (Time(23, 30, 45), Time(2, 15, 20), Time(1, 45, 5)),
    (Time(2, 0, 0), Time(0, 45, 30), Time(2, 45, 30)),
])
def test_addition(time1, time2, expected_sum):
    result = time1 + time2
    assert result == expected_sum
@pytest.mark.parametrize("time1, time2, expected_sup", [
    (Time(5, 30, 45), Time(6, 15, 20), Time(23, 15, 25)),
    (Time(2, 50, 35), Time(0, 45, 30), Time(2, 5, 5)),
])

def test_sub(time1, time2, expected_sup):
    result = time1 - time2
    assert result == expected_sup

@pytest.mark.parametrize("time1, time2", [
    (Time(3, 20, 10), Time(3, 20, 10)),
    (Time(4, 10, 15), Time(4, 10, 15)),
])
def test_equality(time1, time2):
    assert time1 == time2

@pytest.mark.parametrize("time1, time2", [
    (Time(4, 10, 15), Time(4, 10, 20)),
    (Time(1, 30, 45), Time(2, 15, 20)),
])
def test_inequality(time1, time2):
    assert time1 != time2