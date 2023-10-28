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


@pytest.mark.parametrize(
    ('x'),
    [
        [1, 1],
        [1, 2, 5, 1]
    ]
)
def testf(x):
    assert f(x) is False

