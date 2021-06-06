import sys
import pytest

print(sys.version_info)
@pytest.mark.skipif(sys.version_info > (3, 6) , reason="requires python3.6 or higher")
def test_function():
    print("Hello")

def test_1():
    print("Hi")
