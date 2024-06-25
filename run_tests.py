import unittest
from tests.test_google_search import GoogleSearchTest

if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchTest)
    unittest.TextTestRunner(verbosity=2).run(test_suite)