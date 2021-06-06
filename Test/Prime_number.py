import pytest
@pytest.fixture()
def prime():
    for num in range(10,200):
        for i in range(2,10):
            if num%i == 0:
                break
        else:
            print("prime number is=",num)

    return num
print(type(prime))
prime()
#prime(10,20)


def test_a(prime):
    assert prime != 0

