import unittest

import ddeutil.core.base.convert as cc


class ConvertTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.str_true_lists: list[str] = [
            "true",
            "True",
            "1",
            "Y",
            "y",
            "yes",
            "Yes",
        ]
        self.str_false_lists: list[str] = [
            "false",
            "False",
            "0",
            "N",
            "n",
            "no",
            "No",
        ]
        self.str_raise_lists: list[str] = [
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
