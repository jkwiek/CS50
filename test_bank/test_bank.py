from bank import value

def test_hello():
    assert value("hello") == 0
def test_h():
    assert value("hey") == 20
    assert value("howdy") == 20
    assert value("how's it going?") == 20
def test_other():
    assert value("good evening") == 100
    assert value("what's up?") == 100



