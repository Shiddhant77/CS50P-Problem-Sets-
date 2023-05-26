'''
In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂
(otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result.
You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.

'''

def convert(STR):
    STR = STR.replace(":)", '🙂').replace(":(", '🙁')
    return STR

def main():
    user_input = input("Enter anything you like : ")
    user_input = convert(user_input)
    print(user_input)

main()

