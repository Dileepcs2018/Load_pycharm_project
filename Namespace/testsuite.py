import unittest

class sample(unittest.TestCase):
    def setUp(self):
        print("setup method is callled")

    def test_t1(self):
        print("Test1 is executed")

    def test_2(self):
        print("Test2 is executed")


    def tearDown(self):
        print("Teardown execute")


if __name__ == "__main__":
    unittest.main()
