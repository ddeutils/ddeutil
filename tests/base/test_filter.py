import unittest

import ddeutil.core.base.filtering as filtering


class FilteringTestCase(unittest.TestCase):
    def test_filter_dict(self):
        self.assertDictEqual(
            filtering.filter_dict(
                {"foo": "bar"},
                excluded={"foo"},
            ),
            {},
        )
