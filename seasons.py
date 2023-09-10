import datetime
from datetime import date, timedelta
import inflect


class Date:
    # defining init method
    def __init__(self, b_date):
        self._birthdate = b_date

    def __str__(self):
        total_minutes = self.__sub__(None)
        return f"{total_minutes}"

    @classmethod  # creating class method to get the user input
    def get(cls):
        b_date = input("Enter your birthday in YYYY-MM-DD format : ")
        return cls(b_date)

    @property # getter function
    def birthdate(self):
        return self._birthdate

    @birthdate.setter # setter function so that everytime we enter our output gets validated here before it gets assigned
    def birthdate(self, b_date):
        try:
            datetime.datetime.strptime(b_date, "%Y-%m-%d")
            self._birthdate = f"{b_date} 00:00:00"
        except ValueError:
            raise ValueError("Invalid Date format")

    def __sub__(self, other): # overloading the operator
        today = datetime.datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) # assuming that today time is 12 am midnight
        user_input = datetime.datetime.strptime(self._birthdate, "%Y-%m-%d") # parsing the input into date time format
        time_difference = (today - user_input) # subtracting today date with users input
        total_minutes = round(time_difference.total_seconds() / 60) # finding the total second using total_second method and dividing with 60 to get minutes
        return total_minutes

    def conversion(self, total_minutes): # converting minutes in number to minutes in words
        p = inflect.engine() # creating instance of inflect
        words = p.number_to_words(total_minutes, andword="", zero="zero").capitalize()# converting minutes to words and capitalzing the words
        return words


def main():
    # using date1 cause date is built-in datetime module
    date1 = Date.get() # using class methods which will get the run the get class method and create an instance of Date
    time_difference = date1 - None # this is trigger the __sub__ and the calculation would be done there
    print(date1.conversion(time_difference)) # just printing the words


if __name__ == "__main__":
    main()
