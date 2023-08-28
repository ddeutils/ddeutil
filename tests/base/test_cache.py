import unittest

import dup_utils.core.base.cache as cache


class CacheTestCase(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_memoize(self):
        @cache.memoize
        def fib(n):
            if n in (0, 1):
                return 1
            return fib(n - 1) + fib(n - 2)

        for i in range(3):
            fib(i)

        self.assertFalse(fib.cache == {})
        self.assertEqual(fib.cache, {"(0,){}": 1, "(1,){}": 1, "(2,){}": 2})
