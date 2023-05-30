'''
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal,
 don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive.
 For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format,
 to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''
import datetime


def main():
    user_input = input("Enter any time of a day you like : ")
    converted = convert(user_input)
    if converted>=7.00 and converted<8.00:
        print("Eat Breakfast")
    elif converted>=12.00 and converted<13.00:
        print("Eat Lunch")
    elif converted>=18.00 and converted<19.00:
        print("Eat Dinner")
    else:
        print("Not the time to eat!")

def convert(time):
    # What I did here is that ( I mapped int with the user input, when user gave me 12:10 input, I changed it to int and assigned it to hour and minute
    # Split function there is splitting 10:45 into two different list
    hour,minute = map(int, time[:-2].split(':'))  # mapping (int with time)
    indicator = time[-2:]
    if indicator == 'AM' and time[:2] == '12':
        hour+=0
    elif indicator =='PM' and time[:2] !='12': # adding two if pm, meaning if it is 10:00 pm adding 12 and making it 22:00
        hour+=12

    converted_time = hour + minute/60   # converting it into like 7.5 hours
    return converted_time


if __name__ == "__main__":
    main()

