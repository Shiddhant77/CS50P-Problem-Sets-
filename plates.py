'''
Rules
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.
'''

'''
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not
. Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
 wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. 
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

'''
import string
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    character = string.ascii_uppercase
    punctuation = string.punctuation
    if len(s)<2 or len(s)>6:
        return False
    if s[0] not in character and s[1] not in character:
        return  False
    for char in (s):
        if char in punctuation or char == ' ':
            return False
    if s[0]== '0' or s[-1].isalpha():
        return  False

    return  True


main()