__author__ = 'bvenkatesan'

import unittest

class InitializationTests(unittest.TestCase):

    def setUp(self):
        print Exception ("setting up")

    def tearDown(self):
        print("teardown")

    def test_sanity(self):
        """
        check world is sane.. 2 + 2 = 4
        """
        self.assertEquals(2+2,4)

    def test_import(self):
        """
        We are able to import gtcal

        """
        try:
            import gtcal
        except ImportError:
            self.fail("Could not import gtcal")