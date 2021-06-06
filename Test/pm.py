import unittest
from Test import x
class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setup class is called")
    def test_demo(setUpClass):
        print("test is called")

    def test_demo1(setUpClass):
        print("Test2 is called")
    @classmethod
    def tearDownClass(cls):
        print("Tear down method is called")


if __name__ == "__main__":
    unittest.main()