import unittest

import src.dup_utils.core.base.split as split


class SplitTestCase(unittest.TestCase):
    def test_rsplit(self):
        self.assertListEqual(
            ["foo", "bar"], split.rsplit("foo bar", maxsplit=2, mustsplit=False)
        )
