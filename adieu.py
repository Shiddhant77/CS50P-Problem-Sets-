# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
#  names with
#  commas and one and, as in the below:
#
# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
#
# Hints
# Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
# pip install inflect
# import inflect
#
# p = inflect.engine()
#
# list_name = []
#
# while True:
#     try:
#         name = input("Enter a name you like : ")
#         list_name.append(name)
#     except EOFError:
#         break
#
# if len(list_name) == 1:
#     print(f"Adieu, adieu, to {list_name[0]}")
#
# elif len(list_name) == 2:
#     print(f"Adieu, adieu, to {list_name[0]} and {list_name[1]}")
#
# elif len(list_name) > 2:
#     formatted_string = ' , '.join(list_name[:-1])
#     print(f"Adieu, adieu, to {formatted_string}, and {list_name[-1]}")
#

##############################################################################################################
# Code below here is copied from github, above code I did it but couldn't use any of the infect method as required by the question

import inflect

p = inflect.engine()
name_list = []

while True:
    try:
        name = input("Name: ").strip().title()
        name_list.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(name_list))
        break