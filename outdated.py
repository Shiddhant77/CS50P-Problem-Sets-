


# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
#
# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
#
# Hints
# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
# Recall that a list comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
# Note that you can format an int with leading zeroes with code like
# print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.



months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]



while True:
    date = input("Enter the date in (MM-DD-YYYY) order : ")
    if '/' in date: # Checking if / is there or not
        try:
            # If there is  / then when we enter 01/01/2000, then by split it assigns 01 to m, 01 to d and 2000 to y
            m,d,y = map(int,date.split('/'))
        except ValueError:
            print("Invalid date format")
            continue
    else:
        try:
            date_parts = date.split() # we are splitting the input based on whitespace
            month,day,year = map(str.strip,date_parts) # # Then same as above we are assigning it month,day,year
            month = month.capitalize()
            day = day.split(',')[0] # here since we would be inputting date as May 8, 2022 to remove the (,) we are using split
            y = int(year)
            m = months.index(month) + 1  # adding 1 cause index starts from 0 so with +1 it starts with 1
            d = int(day)
        except (ValueError, IndexError) as e:
            print("Invalid date format")
            continue

    if m <1 or m >12 or d > 31 or d<1 or y<1:
        print("Invalid date")
        continue

    converted_date = f"{y:04d}-{m:02d}-{d:02d}" # we are now assigning how many integer we need
    print(f"The converted date is {converted_date}")
    break













