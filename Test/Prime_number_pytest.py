import pytest
lst1 = []

def prime():
    start = 10
    end = 50
    for num in range(start,end):
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print("Prime number is=",num)
            lst1.append(num)
    return lst1

z = prime()
print("Value of prime number is =", z)

def test_prime():
    assert lst1[0] ==11,"fail"
