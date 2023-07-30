from fuel_unit_test import convert, gauge
import pytest
def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/2") == pytest.approx(50)
    assert convert("99/100") == pytest.approx(99)
    assert convert("1/100") == pytest.approx(1)


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(90)=="90%"

if __name__ == '__main__':
    main()