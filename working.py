import re
import sys
def main():
    s= input("Enter time in 12-hour format : ").replace('A.M','AM').upper().replace('P.M', 'PM')
    a = convert(s)
    print(a)
def convert(s):
    try:
        pattern = r"([0-9]{1,2})(?:\:)?([0-9]{1,2})? (AM|PM) to ([0-9]{1,2})(?:\:)?([0-9]{1,2})? (AM|PM)"
        match = re.search(pattern,s,re.IGNORECASE)
        if match:
            if int(match.group(1)) == 12:
                first_match = 00
            else:
                first_match = int(match.group(1))
            third_match = match.group(3)
            if int(match.group(4)) ==12:
                fourth_match = 00
            else:
                fourth_match = int(match.group(4))
            sixth_match = match.group(6)
            if match.group(2) == None and match.group(5) == None:
                a = new_convert(first_match,third_match,fourth_match,sixth_match)
                return a
            else:
                second_match = int(match.group(2))
                fifth_match = int(match.group(5))
            if first_match >13 and second_match >60 and fourth_match>13 and fifth_match >60:
                raise ValueError("Invalid Time format")
            else:
                if third_match == 'AM' and sixth_match == 'AM':
                    return f"{first_match:02}:{second_match:02} to {fourth_match:02}:{fifth_match:02}"
                elif third_match == 'PM' and sixth_match == 'PM':
                    first_match +=12
                    fourth_match +=12
                    return f"{first_match:02}:{second_match:02} to {fourth_match:02}:{fifth_match:02}"
                elif third_match == 'AM' and sixth_match =='PM':
                    fourth_match+=12
                    return f"{first_match:02}:{second_match:02} to {fourth_match:02}:{fifth_match:02}"
                elif third_match=='PM' and sixth_match== 'AM':
                    first_match+=12
                    return f"{first_match:02}:{second_match:02} to {fourth_match:02}:{fifth_match:02}"
        else:
            print("No match found")
    except ValueError:
        print("Invalid format")
def new_convert(first_match,third_match,fourth_match,sixth_match):
            if first_match >13 and fourth_match>13 :
                raise ValueError("Invalid Time format")
            else:
                if third_match == 'AM' and sixth_match == 'AM':
                    return f"{first_match:02}:00 to {fourth_match:02}:00"
                elif third_match == 'PM' and sixth_match == 'PM':
                    first_match +=12
                    fourth_match +=12
                    return f"{first_match:02}:00 to {fourth_match:02}:00"
                elif third_match == 'AM' and sixth_match =='PM':
                    fourth_match+=12
                    return f"{first_match:02}:00 to {fourth_match:02}:00"
                elif third_match=='PM' and sixth_match== 'AM':
                    first_match+=12
                    return f"{first_match:02}:00 to {fourth_match:02}:00"
if __name__ == "__main__":
    main()


