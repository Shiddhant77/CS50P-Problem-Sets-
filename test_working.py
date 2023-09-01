from working import convert,new_convert
import pytest

def main():
    test_convert()
    test_new_convert()
def test_convert():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10:20 AM to 9:30 PM') == '10:20 to 21:30'
    assert convert('12:50 AM to 12:30 PM') == '00:50 to 12:30'

def test_new_convert():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 AM to 12 PM') == '10:00 to 12:00'
    assert convert('12 AM to 10 PM') == '00:00 to 22:00'




if __name__ == "__main__":
    main()
