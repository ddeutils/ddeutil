import unittest

import ddeutil.core.base.prepare as pp


class PrepareTestCase(unittest.TestCase):
    def test_round_up(self):
        self.assertEqual(pp.round_up(1.00406, 2), 1.01)
        self.assertEqual(pp.round_up(1.00001, 1), 1.1)

    def test_remove_pad(self):
        self.assertEqual(pp.remove_pad("000"), "0")
        self.assertEqual(pp.remove_pad("12"), "12")
