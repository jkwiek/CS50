from plates import is_valid

def test_length():
    assert is_valid("CAT") == True
    assert is_valid("C") == False
    assert is_valid("caterpillar") == False
def test_beginning():
    assert is_valid("AB12") == True
    assert is_valid("C139") == False
    assert is_valid("123456") == False
def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AB12CD") == False
def test_characters():
    assert is_valid("HI!!") == False
    assert is_valid(".?!:") == False
