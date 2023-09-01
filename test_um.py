from um import count

def main():
    test_count()

def test_count():
    assert count('Hello, um my name is UM, how are you um, let\'s eat something yummy') == 3
    assert count('um is my good ummy, UM, Um, Um') == 4



if __name__ == "__main__":
    main()

