from bank import value

def test_value_zero():
    assert value("здравствуйте, как дела?") == 0
    assert value("здравствуйте, что нового?") == 0

def test_value_twenty():
    assert value("зайти в магазин") == 20
    assert value("забрать посылку") == 20

def test_value_hundred():
    assert value("привет, как дела?") == 100
    assert value("Закончить работу") == 100
