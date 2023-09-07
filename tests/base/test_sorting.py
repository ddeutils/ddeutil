import unittest

import ddeutil.core.base.sorting as sorting


class SortingTestCase(unittest.TestCase):
    def test_ordered(self):
        result = sorting.ordered([[11], [2], [4, 1]])
        respect = [[1, 4], [2], [11]]
        for i in range(3):
            self.assertEqual(result[i], respect[i])
