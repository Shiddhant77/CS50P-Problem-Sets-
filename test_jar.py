from jar import Jar
from unittest.mock import Mock
import pytest


def main():
    test_str()
    test_deposit()
    test_withdraw()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(10)
    assert str(jar) == "🍪🍪"


def test_deposit():
    jar = Jar()
    jar.capacity = 10
    jar._cookies = 5
    jar.deposit = Mock(wraps=jar.deposit)
    jar.deposit(3)
    jar.deposit.assert_called_with(3)
    assert jar._cookies == 8


def test_withdraw():
    jar = Jar()
    jar.capacity = 10
    jar._cookies = 5
    jar.withdraw = Mock(wraps=jar.withdraw)
    jar.withdraw(3)
    jar.withdraw.assert_called_with(3)
    assert jar._cookies == 2


if __name__ == "__main__":
    pytest.main(["test_jar.py"])
