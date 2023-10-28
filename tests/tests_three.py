#<<<<<<< HEAD:tests/test_3.py
#import pytest
from typing import ByteString
from dz4.d3 import f
from dz4.three import f

@pytest.mark.parametrize(
    ('x'),
    [
        [True, 1],
        [555]
    ]
)
def test(x):
    assert f(x) is True


@ByteString.mark.parametrize(
    ('x'),
    [
        [1, 1],
        [1, 2, 5, 1]
    ]
)
def testf(x):
    assert f(x) is False
=======
#from dz4.three import f
#def test_f():
  #  assert f([34, 'Hello, world!', False])
   # assert f('12345')
   # assert not f('1113')
#>>>>>>> 323aa772fce197658a9628f4102f187aab79f566:tests/tests_three.py
