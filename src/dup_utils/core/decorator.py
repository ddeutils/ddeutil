import contextlib
import copy
from functools import wraps
from time import time

from src.dup_utils.core.base.check_convert import round_up


def deepcopy_params(func):
    """Deep copy function

    :usage:
        >>> @deepcopy_params
        ... def test(a, b, c = None ):
        ...     c = c or {}
        ...     a[1] = 3
        ...     b[2] = 4
        ...     c[3] = 5
        ...     return a, b, c
        >>> aa = {1: 2}
        >>> bb = {2: 3}
        >>> cc = {3: 4}
        >>> test(aa, bb, cc)
        ({1: 3}, {2: 4}, {3: 5})

    """

    def func_get(self, *args, **kwargs):
        return func(
            self,
            *(copy.deepcopy(x) for x in args),
            **{k: copy.deepcopy(v) for k, v in kwargs.items()},
        )

    return func_get


class classproperty:
    """Decorator that converts a method with a single cls argument into a property
    that can be accessed directly from the class.
    """

    def __init__(self, method=None):
        self.fget = method

    def __get__(self, instance, cls=None):
        return self.fget(cls)

    def getter(self, method):
        self.fget = method
        return self


class ClassPropertyDescriptor:
    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        return self.fget.__get__(obj, klass)()

    def __set__(self, obj, value):
        if not self.fset:
            raise AttributeError("can't set attribute")
        type_ = type(obj)
        return self.fset.__get__(obj, type_)(value)

    def setter(self, func):
        if not isinstance(func, (classmethod, staticmethod)):
            func = classmethod(func)
        self.fset = func
        return self


def class_property(func):
    if not isinstance(func, (classmethod, staticmethod)):
        func = classmethod(func)
    return ClassPropertyDescriptor(func)


def timing_decorator(name):
    def timing_internal(func):
        @wraps(func)
        def wrap(*args, **kw):
            print(f"Step '{name}' start", flush=True)
            time_start = time()
            result = func(*args, **kw)
            time_end = time()
            print(
                f"Step '{name}' took: {round_up(time_end - time_start, 2)} sec",
                flush=True,
            )
            return result

        return wrap

    return timing_internal


@contextlib.contextmanager
def measure_performance(title):
    """
    :usage:
        >>> import time
        >>> with measure_performance('test'):
        ...     time.sleep(2)
        test ....................................................... 2.00s
    """
    ts = time()
    yield
    te = time()
    padded_name = f"{title} ".ljust(60, ".")
    padded_time = f" {(te - ts):0.2f}".rjust(6, ".")
    print(f"{padded_name}{padded_time}s", flush=True)
