'''
 implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due.
 Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
  Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
'''

loop = True
total = 0
amount_due = 50
change_owe = 0
while loop:
    coin = int(input("Enter amount in 25, 10 ,5 : "))
    if coin == 25 or coin == 10 or coin == 5:
        amount_due = amount_due - coin
        total = total + coin
        print(f"Amount due : {amount_due}")
        if amount_due <=0:
            change_owe = total - 50
            print(f"Change owed : {change_owe}")
            loop = False
    else:
        print(f"Amount due : {amount_due} ")






