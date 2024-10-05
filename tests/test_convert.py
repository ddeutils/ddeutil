import pytest
from ddeutil.core import convert as cc


def test_str2bool():
    assert not cc.str2bool()

    for _string in ["true", "True", "1", "Y", "y", "yes", "Yes", "o", "O"]:
        assert cc.str2bool(_string)

    for _string in ["false", "False", "0", "N", "n", "no", "No", "x", "X"]:
        assert not cc.str2bool(_string)

    assert not cc.str2bool("Nop", force_raise=False)


def test_str2bool_raise():
    with pytest.raises(ValueError):
        cc.str2bool("Nop")


def test_str2list():
    assert cc.str2list() == []
    assert cc.str2list('["a", "b", "c"]') == ["a", "b", "c"]
    assert cc.str2list('["d""]', force_raise=False) == ['["d""]']
    assert cc.str2list('"d""]', force_raise=False) == ['"d""]']

    with pytest.raises(ValueError):
        cc.str2list('["d""]')

    with pytest.raises(ValueError):
        cc.str2list('"d""]')


def test_str2dict():
    assert cc.str2dict() == {}
    assert cc.str2dict('{"a": 1, "b": 2, "c": 3}') == {"a": 1, "b": 2, "c": 3}
    assert cc.str2dict('{"d""}', force_raise=False) == {1: '{"d""}'}

    with pytest.raises(ValueError):
        cc.str2dict('{"d""}')
