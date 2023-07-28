from bank_unit_test import value

def main():
    test_bank_value()

def test_bank_value():
    assert value('hey, there') == 20
    assert value("hello, how are you ") == 0
    assert value("No way") ==100

if __name__ == '__main__':
    main()