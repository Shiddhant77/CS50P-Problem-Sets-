import re
import sys


def main():
    ip = sys.argv[1]
    if validate(ip):
        print(True)
    else:
        print(False)


def validate(ip):
    pattern = r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})"
    match = re.search(pattern,ip)
    if match:
        first_part = int(match.group(1))
        second_part = int(match.group(2))
        third_part = int(match.group(3))
        fourth_part = int(match.group(4))
        if first_part > 255 or first_part < 0:
            print("Invalid IP")
        elif second_part > 255 or second_part < 0:
            print("Invalid IP")
        elif third_part > 255 or third_part < 0:
            print("Invalid IP")
        elif fourth_part > 255 or fourth_part < 0:
            print("Invalid IP")
        else:
            print(f"Your IP address {first_part}.{second_part}.{third_part}.{fourth_part} is valid ")
    else:
        print("Invalid IP format")

    return ip


if __name__ == "__main__":
    main()