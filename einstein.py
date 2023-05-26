'''
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

'''


mass = int(input("Enter any number you like to calculate : "))

energy = mass * 299792458**2
print(energy)

