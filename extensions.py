'''
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that
 file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
'''


user_input = input("Enter any file name with extension you like : ")

if user_input.endswith('.gif'):
    print('image/gif')
elif user_input.endswith('.jpeg') or user_input.endswith('.jpg'):
    print('image/jpeg')
elif user_input.endswith('.png'):
    print('image/png')
elif user_input.endswith('.pdf'):
    print('application/pdf')
elif user_input.endswith('.txt'):
    print('text/plain')
elif user_input.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
