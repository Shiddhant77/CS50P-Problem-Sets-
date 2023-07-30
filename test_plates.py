from plates_unit_test import is_valid

def main():
    test_is_valid()
    test_is_valid_two()
    test_is_valid_more()
def test_is_valid():
    assert is_valid('CS50') == True
    assert is_valid('CS5P') == False

def test_is_valid_two():
    assert is_valid('CS') == True
    assert is_valid('5')== False
    assert is_valid('C5') ==False

def test_is_valid_more():
    assert is_valid('AAA222')==True
    assert is_valid('AAA2AA') == False
    assert is_valid('CS50CS') == False


if __name__ == '__main__':
    main()