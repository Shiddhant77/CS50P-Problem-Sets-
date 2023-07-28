def main():
    greeting = input("Enter anything you like : ")
    returned_value = value(greeting)
    print(f"The returned value is {returned_value}")


def value(greeting):
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()