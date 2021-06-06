from Namespace.testsuite import sample
import unittest

tc1 = unittest.TestLoader().loadTestsFromTestCase(sample)
test_suite = unittest.TestSuite([tc1])
unittest.TextTestRunner().run(test_suite)

