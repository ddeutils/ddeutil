import unittest
from typing import List

import src.dup_utils.core.base.check_convert as cc


class CheckTestCase(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_is_int(self):
        map_value_respect = (
            (1, True),
            (-1, True),
            (1.0, False),
            (-1.0, False),
            ("0", True),
            ("1", True),
            ("-1", True),
            ("+1", True),
            ("06", True),
            ("abc 123", False),
            (1.1, False),
            (-1.1, False),
            ("1.1", False),
            ("-1.1", False),
            ("+1.1", False),
            ("1.1.1", False),
            ("1.1.0", False),
            ("1.0.1", False),
            ("1.0.0", False),
            ("1.0.", False),
            ("1..0", False),
            ("1..", False),
            ("0.0.", False),
            ("0..0", False),
            ("0..", False),
            ("one", False),
            (object(), False),
            ((1, 2, 3), False),
            ([1, 2, 3], False),
            ({"one": "two"}, False),
            ("0.", False),
            (".0", False),
            (".01", False),
        )
        for values in map_value_respect:
            _respec, _value = values[1], values[0]
            self.assertEqual(_respec, cc.is_int(_value))

    def test_can_int(self):
        map_value_respect = (
            (1, True),
            (-1, True),
            (1.0, True),
            (-1.0, True),
            ("0.", True),
            ("0.0", True),
            ("1.0", True),
            ("-1.0", True),
            ("+1.0", True),
        )
        for values in map_value_respect:
            _respec, _value = values[1], values[0]
            self.assertEqual(_respec, cc.can_int(_value))


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
            "x",
            "X",
        ]

    def test_convert_str2bool(self):
        for _string in self.str_true_lists:
            self.assertTrue(cc.str2bool(_string))

        for _string in self.str_false_lists:
            self.assertFalse(cc.str2bool(_string))

        for _string in self.str_raise_lists:
            self.assertRaises(ValueError, cc.str2bool, _string)
