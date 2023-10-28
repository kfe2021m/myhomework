#<<<<<<< HEAD:tests/test_2.py
#import pytest
from dz4.d2 import cn


@pytest.mark.parametrize(
    ('n', 'end'),
    [
        (5, 120),
        (4, 24),
        (0, 1)
    ]
)
def test(n, end):
    assert cn(n) == end
#=======
#from dz4.two import fac
#def test_fac():
   # assert fac(0) == 1
   # assert fac(1) == 1
    #assert fac(5) == 120
#>>>>>>> 323aa772fce197658a9628f4102f187aab79f566:tests/tests_two.py
