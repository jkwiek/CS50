from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        convert("5/2")
        convert("3.4/5")
        convert("1/cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_gauge():
    assert gauge("0") == "E"
    assert gauge("1") == "E"
    assert gauge("100") == "F"
    assert gauge("99") == "F"
    assert gauge("50") == "50%"



