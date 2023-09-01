import re
import sys


def main():
    s = input("Text : ")
    a = count(s)
    print(a)

def count(s):
    pattern = r'(\bum\b)'
    matches = re.findall(pattern,s,re.IGNORECASE)
    lower_matches = [i.lower() for i in matches]
    count_variable = 0
    for j in lower_matches:
        if 'um' in j:
            count_variable+=1
        else:
            pass
    if count_variable==0:
        return 0
    else:
        return count_variable





if __name__ == "__main__":
    main()