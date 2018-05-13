from validator import dummy_func


def test_dummy_func():
    assert dummy_func() == True
    assert dummy_func() != False
