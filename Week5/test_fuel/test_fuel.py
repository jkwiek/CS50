from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99.5) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


def test_convert_valueError():
    with pytest.raises(ValueError):
        assert convert("5/2")
        assert convert("3.4/5")
        assert convert("1/cat")

def test_convert_ZeroError():
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")
'
