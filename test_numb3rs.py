from numb3rs import validate

import pytest


def main():
    test_validate()

def test_validate():
    assert validate('192.168.1.1') == '192.168.1.1'
    assert validate('270.10.1.1') == '270.10.1.1'
    assert validate('100.100.100.1') == '100.100.100.1'

if __name__ == '__main__':
    main()