import logging
import unittest
from typing import Any, Dict, List, Literal, Tuple

import src.dup_utils.core.base.check_convert as cc

TestCaseMap = Literal["value", "respec"]


class CheckTestCase(unittest.TestCase):
    def test_check_int(self):
        map_value_respect: Tuple[Dict[TestCaseMap, Any], ...] = (
            {"value": 1, "respec": True},
            {"value": -1, "respec": True},
            {"value": 1.0, "respec": True},
            {"value": -1.0, "respec": True},
            {"value": "0", "respec": True},
            {"value": "0.", "respec": False},
            {"value": "0.0", "respec": False},
            {"value": "1", "respec": True},
            {"value": "-1", "respec": True},
            {"value": "+1", "respec": True},
            {"value": "1.0", "respec": False},
            {"value": "-1.0", "respec": False},
            {"value": "+1.0", "respec": False},
            {"value": "06", "respec": True},
            {"value": "abc 123", "respec": False},
            {"value": 1.1, "respec": True},
            {"value": -1.1, "respec": True},
            {"value": "1.1", "respec": False},
            {"value": "-1.1", "respec": False},
            {"value": "+1.1", "respec": False},
            {"value": "1.1.1", "respec": False},
            {"value": "1.1.0", "respec": False},
            {"value": "1.0.1", "respec": False},
            {"value": "1.0.0", "respec": False},
            {"value": "1.0.", "respec": False},
            {"value": "1..0", "respec": False},
            {"value": "1..", "respec": False},
            {"value": "0.0.", "respec": False},
            {"value": "0..0", "respec": False},
            {"value": "0..", "respec": False},
            {"value": "one", "respec": False},
            {"value": object(), "respec": False},
            {"value": (1, 2, 3), "respec": False},
            {"value": [1, 2, 3], "respec": False},
            {"value": {"one": "two"}, "respec": False},
            {"value": "0", "respec": True},
            {"value": "0.", "respec": False},
            {"value": ".0", "respec": False},
            {"value": ".01", "respec": False},
        )
        for value in map_value_respect:
            self.assertEqual(value["respec"], cc.check_int(value["value"]))


class ConvertTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s %(module)s %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

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

    def test_convert_to_bool(self):
        for _string in self.str_true_lists:
            self.assertTrue(cc.convert_str_to_bool(_string))

        for _string in self.str_false_lists:
            self.assertFalse(cc.convert_str_to_bool(_string))

        for _string in self.str_raise_lists:
            self.assertRaises(ValueError, cc.convert_str_to_bool, _string)
