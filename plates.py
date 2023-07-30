import string

def main():
    s = input("Enter you plate number : ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) <2 or len(s)>6:

        return False
    elif s[0] not in string.ascii_letters or s[1] not in string.ascii_letters:
        return False
    for i in s:
        if i in string.punctuation:
            return False
    for i in s:
        if i.isdigit() and s[-1].isalpha():
            return False
    if s.startswith('0'):
        return False

    return True


if __name__ == "__main__":
    main()
