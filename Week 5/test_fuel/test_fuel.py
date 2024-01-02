from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == "50"
    assert convert("1/3") == "33"
    convert("5/2") raises ValueError
    convert("3.4/5") raises ValueError
    convert("1/cat") raises ValueError
    convert("1/0") raises ZeroDivisionError
def test_gauge():
    assert gauge("0") == "E"
    assert gauge("1") == "E"
    assert gauge("100") == "F"
    assert gauge("99") == "F"
    assert gauge("50") == "50%"

#convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
#gauge expects an int and returns a str that is:
#"E" if that int is less than or equal to 1,
#"F" if that int is greater than or equal to 99,
#and "Z%" otherwise, wherein Z is that same int.
