from dz4.d3 import f
def test_f():
    assert f([34, 'Hello, world!', False])
    assert f('12345')
    assert not f('1113')