'''
implement a program that prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
'''

user_input = input("Enter any string you like : ").lower()
for char in user_input:
    if char =='a' or char=='e' or char=='i' or char=='o' or char=='u':
        user_input = user_input.replace(char,'')
print(user_input)