import unittest
from typing import (
    Any,
    Callable,
    NoReturn,
    Optional,
    Union,
)

from ddeutil.core.base import isinstance_check, remove_pad, round_up


class BaseTestCase(unittest.TestCase):
    def test_instance_check(self):
        self.assertTrue(isinstance_check("s", str))
        self.assertTrue(isinstance_check(["s"], list[str]))
        self.assertTrue(isinstance_check(("s", "t"), tuple[str, ...]))
        self.assertTrue(not isinstance_check(("s", "t"), tuple[str]))
        self.assertTrue(
            isinstance_check({"s": 1, "d": "r"}, dict[str, Union[int, str]])
        )
        self.assertTrue(isinstance_check("s", Optional[str]))
        self.assertTrue(isinstance_check(1, Optional[Union[str, int]]))
        self.assertTrue(not isinstance_check("s", list[str]))
        self.assertTrue(isinstance_check([1, "2"], list[Union[str, int]]))
        self.assertTrue(not isinstance_check("s", NoReturn))
        self.assertTrue(isinstance_check(None, NoReturn))
        self.assertTrue(isinstance_check("A", Any))
        self.assertTrue(
            isinstance_check([1, [1, 2, 3]], list[Union[list[int], int]])
        )

    def test_instance_generic(self):
        def caller() -> str:
            return "Success"

        self.assertTrue(isinstance_check(caller, Callable[[], str]))
        self.assertTrue(isinstance_check(caller, Callable[[str], str]))
        self.assertTrue(not isinstance_check(caller(), Callable[[], str]))


class BasePrepareTestCase(unittest.TestCase):
    def test_round_up(self):
        self.assertEqual(round_up(1.00406, 2), 1.01)
        self.assertEqual(round_up(1.00001, 1), 1.1)

    def test_remove_pad(self):
        self.assertEqual(remove_pad("000"), "0")
        self.assertEqual(remove_pad("12"), "12")
