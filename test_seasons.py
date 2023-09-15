from seasons import Date
import pytest
from unittest.mock import Mock


def main():
    test_birthdate()
    test_sub()


def test_birthdate():
    date = Date("2020-10-20")
    assert date.birthdate == "2020-10-20"

def test_sub():
    date= Date("2020-10-20")
    age = date - None
    expected_result = 1526400
    assert age == expected_result


if __name__ == "__main__":
    pytest.main(["test_seasons.py"])
