import re
import sys


def main():
    s = input("HTML : ")
    a=parse(s)
    print(a)


def parse(s):
    pattern = r'(https?)?://(?:www\.|\w+\.)?(?:youtube)\.com/(?:\w+)/(\w+)["\']?'
    match = re.search(pattern,s,re.IGNORECASE)
    if match:
        if match.group(1) == "http":
            return f"http://youtu.be/{match.group(2)}"
        elif match.group(1)=="https":
            return f"https://youtu.be/{match.group(2)}"
    else:
        sys.exit("No match ")





if __name__ == "__main__":
    main()


#    pattern = r'(?:iframe)?(?:\w+)?(?:src=)?[\"]?["\']?(https?)?://(?:www\.|\w+\.)?(?:youtube)\.com/(?:\w+)/(\w+)["\']?'
