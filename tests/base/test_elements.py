import logging
import unittest
from typing import List

import dup_utils.core.base.elements as elements


class ConvertTestCase(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s %(module)s %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )

    def setUp(self) -> None:
        self.fix_list: list = ["a", "b", "c"]
        self.input_lists: List[list] = [
            [
                "a",
                "e",
                "f",
            ],
            ["e", "f"],
            ["a", "b", "e"],
        ]
        self.output_lists: list = ["a", "a", "a"]

    def test_only_one_with_default(self):
        for index, _list in enumerate(self.input_lists, start=0):
            self.assertEqual(
                self.output_lists[index],
                elements.only_one(_list, self.fix_list),
            )
