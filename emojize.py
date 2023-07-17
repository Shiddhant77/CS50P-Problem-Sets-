import emoji
user_input = input("Enter the emoji you want : ")

converted = emoji.emojize(user_input, language='alias')
print(f"Output : {converted} ")
