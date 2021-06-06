import pytest
@pytest.mark.parametrize("num",[10,20,30,40])

def test_foo(num):
    assert num > 0



