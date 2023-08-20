import unittest
from typing import List

import src.dup_utils.core.base.convert as cc


class ConvertTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.str_true_lists: List[str] = [
            "true",
            "True",
            "1",
            "Y",
            "y",
            "yes",
            "Yes",
        ]
        self.str_false_lists: List[str] = [
            "false",
            "False",
            "0",
            "N",
            "n",
            "no",
            "No",
        ]
        self.str_raise_lists: List[str] = [
            # "x",
            # "X",
            "Nop",
        ]

    def test_convert_str2bool(self):
        for _string in self.str_true_lists:
            self.assertTrue(cc.str2bool(_string))

        for _string in self.str_false_lists:
            self.assertFalse(cc.str2bool(_string))

        for _string in self.str_raise_lists:
            self.assertRaises(ValueError, cc.str2bool, _string)
