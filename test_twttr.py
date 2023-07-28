from twttr_unit_test import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("onion") == "nn"
    assert shorten("electricity") == "lctrcty"
    assert shorten("apple") == "ppl"

if __name__ == '__main__':
    main()