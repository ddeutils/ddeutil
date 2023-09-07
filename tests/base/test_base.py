import unittest
from typing import (
    Any,
    Callable,
    Dict,
    List,
    NoReturn,
    Optional,
    Tuple,
    Union,
)

from ddeutil.core.base import isinstance_check


class BaseTestCase(unittest.TestCase):
    def test_instance_check(self):
        self.assertTrue(isinstance_check("s", str))
        self.assertTrue(
            isinstance_check(
                [
                    "s",
                ],
                List[str],
            )
        )
        self.assertTrue(
            isinstance_check(
                (
                    "s",
                    "t",
                ),
                Tuple[str, ...],
            )
        )
        self.assertTrue(
            not isinstance_check(
                (
                    "s",
                    "t",
                ),
                Tuple[str],
            )
        )
        self.assertTrue(
            isinstance_check({"s": 1, "d": "r"}, Dict[str, Union[int, str]])
        )
        self.assertTrue(isinstance_check("s", Optional[str]))
        self.assertTrue(isinstance_check(1, Optional[Union[str, int]]))
        self.assertTrue(not isinstance_check("s", List[str]))
        self.assertTrue(isinstance_check([1, "2"], List[Union[str, int]]))
        self.assertTrue(not isinstance_check("s", NoReturn))
        self.assertTrue(isinstance_check(None, NoReturn))
        self.assertTrue(isinstance_check("A", Any))
        self.assertTrue(
            isinstance_check([1, [1, 2, 3]], List[Union[List[int], int]])
        )

    def test_instance_generic(self):
        def caller():
            return "Success"

        self.assertTrue(isinstance_check(caller, Callable[[], str]))
        self.assertTrue(isinstance_check(caller, Callable[[str], str]))
        self.assertTrue(not isinstance_check(caller(), Callable[[], str]))
