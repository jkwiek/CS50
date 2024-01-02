from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(99.5) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/2") == "50"
