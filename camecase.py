# '''
# , implement a program that prompts the user for the name of a variable in camel case and
#  outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
#
# '''

user_input= input("Enter camel case word")

for letter in range(len(user_input)):
    if user_input[letter].isupper():
        user_input= user_input[:letter] + '_' + user_input[letter].lower()+ user_input[letter+1::]

print(user_input)