# from pyfiglet import Figlet
# import sys
# import random
#
# a = input("Enter -f or --font : ")
# b = input("Choose the font you want : ")
# figlet = Figlet()
#
# random_fonts = figlet.getFonts()
# print(random_fonts)
#
# if a=='':
#     c = input("Enter your text that you would like to convert : ")
#
#     select_font= random.choice(random_fonts)
#     figlet = Figlet(font=select_font)
#     print(figlet.renderText(c,select_font))
#
#
# elif (a =='-f' or a=='--font') and (b in random_fonts):
#     c = input("Enter your text that you would like to convert : ")
#     figlet = Figlet(font=b)
#     print(figlet.renderText(c))
#
# else:
#     sys.exit("Please provide correct details! ")
#


from pyfiglet import Figlet
import  sys
import  random
figlet = Figlet()
random_font = figlet.getFonts()
if len(sys.argv) == 1:

    select_random_font = random.choice(random_font)
    figlet = Figlet(font=select_random_font)
    text = input("Enter the text you want to change :  ")
    print(figlet.renderText(text))

elif (len(sys.argv)==3) and (sys.argv[1]=='-f' or sys.argv[1]=='--font'):
    select_random_font = sys.argv[2]
    if select_random_font in random_font:

        figlet = Figlet(font=select_random_font)
        text = input("Enter the text you want to change : ")
        print(figlet.renderText(text))
    else:
        sys.exit("Please enter valid font !")
else:
    sys.exit("Please enter correct details !")


