import pytest
lst1 = []
def Prime():
    start = 10
    end = 200
    for num in range(start,end):
        for i in range(2,num):
            if num %i == 0:
                break
        else:
            print("Value of prime number is=",num)


Prime()