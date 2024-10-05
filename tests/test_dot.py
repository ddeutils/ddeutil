import pytest
from ddeutil.core import getdot


def test_getdot():
    assert getdot("data.value", {"data": {"value": 1}}) == 1
    assert getdot("data", {"data": "test"}) == "test"

    with pytest.raises(ValueError):
        getdot("data.value", {"data": "test"})

    assert getdot("data.value", {"data": {"key": 1}}, None) is None

    assert (
        getdot(
            "data.value.getter",
            {"data": {"value": {"getter": "success", "put": "fail"}}},
        )
        == "success"
    )

    assert getdot("foo.bar", {"foo": {"baz": 1}}, ignore=True) is None

    assert getdot("foo.bar", {"foo": {"baz": 1}}, 2, 3) == 2
    assert getdot("foo.bar", {"foo": {"baz": 1}}, 2, 3, ignore=True) == 2

    assert getdot("test?.error", {"foo": "bar"}) is None
    assert getdot("test.error?.message", {"test": {"bar": {}}}) is None
