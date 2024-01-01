from twttr import shorten

def test_allLower():
    assert shorten("monday") == "mndy"
    assert shorten("tuesday") == "tsdy"

def test_allUpper():
    assert shorten("WEDNESDAY") == "WDNSDY"
    assert shorten("THURSDAY") == "THRSDY"

def test_numbers():
    assert shorten("12345") == "12345"

def test_mix():
    assert shorten("Cs50") == "Cs50"
    assert shorten("Friday13") == "Frdy13"
