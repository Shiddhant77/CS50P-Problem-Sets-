'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
 outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
'''

user_input = input("What is the Great Question of Life, the Universe and Everything, : ").lower()

if user_input == '42' or user_input == 'forty-two' or user_input == 'forty two':
    print('YES')
else:
    print('NO')

