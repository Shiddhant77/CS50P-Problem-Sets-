class Jar:
    def __init__(self, capacity=12):  # initilizing the instance of class
        self.capacity = capacity
        self._cookies = 0


    def __str__(self):    # str is used when we want to print the instance of class. If not used we would get output as memory location
        return "🍪" * self._cookies

    def deposit(self, n): # adding cookies into capacity
        if self._cookies + n > self._capacity: # checking if we deposit cookies will our total get over capacity or not
            raise ValueError("Capacity exceeded") # if it exceeds then raise error
        self._cookies += n # else add cookies


    def withdraw(self, n): # withdraw cookies into capacity
        if self._capacity < n: # checking if there are enough cookies to withdraw or not
            raise ValueError("Not enough cookies to withdraw") # if not then raise error
        self._cookies -= n # else withdraw cookies from total capacity
    @property
    def capacity(self): # defining total capacity the container can hold
        return self._capacity

    @capacity.setter
    def capacity(self, capacity): # checking if the user has provided  what is required
        if not isinstance(capacity, int) or capacity < 0: # checking if the number provided is instance of class (int is class) and checking if number is less than 0 or not
            raise ValueError("Capacity must be a non-negative integer") # raising error if either of condition does not match
        self._capacity = capacity # else assigning capacity the correct value

    @property
    def size(self):
        return self._cookies # returning the total number of cookies


def main():
    jar = Jar() # creating the instance of class
    jar.capacity = int(input("Enter the number of cookies you want : ")) # assigning value to capacity
    while True:
        action = input("What do you want to do (deposit/withdraw/quit) : ").lower()
        ''' Based on action provided, executing the required function'''
        if action == "quit" or action == "q":
            break
        try:
            n = int(input("Enter the number of cookies : ")) # asking how many cookies the user wants to add or remove
            if action == "deposit" or action == "d": # if d or deposit then add
                jar.deposit(n)
            elif action == "withdraw" or action == "w": # if w or withdraw then remove the cookies
                jar.withdraw(n)
        except ValueError as e: # catching any error
            print(e)
    print(f"Total cookies {jar}") # printing the total number of cookies


if __name__ == "__main__":
    main()
