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


   




    
#     assert test_input_time()==1
#    # t = Time()
#     ##user_input = ["5", "30", "45"]
#    # def mock_input(prompt):
#        # return user_input.pop(0)

#     mocker.patch('builtins.input', mock_input)
#     t.input_time()

#     assert t.hours == 5
#     assert t.minutes == 30
#     assert t.seconds == 45
# def test__str__time(capsys):
#     t = Time(12, 5, 30)
#     t.display_time()
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "Время: 12:05:30"

# def test_input_time(mocker):
#     mocker.patch('input_time', return_value = 1)
#     assert input_time()