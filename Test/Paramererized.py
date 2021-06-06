import pytest

@pytest.mark.parametrize("num1",[1,2,3,4,5])
def test_a1(num1):
    assert num1 >0

