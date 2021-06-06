import unittest
from Namespace.testsuite import sample

tc1 = unittest.TestLoader().loadTestsFromTestCase(sample)
tc2 = unittest.TestLoader().loadTestsFromTestCase(sample)

test_suite = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner().run(test_suite)