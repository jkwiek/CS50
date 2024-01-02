from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HEllO") == 0
def test_h():
    assert value("hey") == 20
    assert value("HOWDY") == 20
    assert value("how's it going?") == 20
def test_other():
    assert value("Good Evening") == 100
    assert value("what's up?") == 100



