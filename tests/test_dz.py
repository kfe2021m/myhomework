from dz8.dz import Time

def test_input_time(mocker):
    mocker.patch('builtins.input', return_value = 1)
    t = Time()
    t.input_time()
    assert t.hours == 1
    assert t.minutes == 1
    assert t.seconds == 1

def test_str_(mocker):
    t = Time(1,1,1)
    assert str(t) == 'Время: 01:01:01'