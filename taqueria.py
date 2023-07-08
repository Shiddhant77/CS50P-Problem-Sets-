
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0

while True:
    try:
        item = input("What would you like to have : ")
    except EOFError:
        print("Thank you for ordering")
        break

    for key,value in menu.items():
        if item == key:
            total = total + value

            break

    else:
        print("The item is not on the menu")

print(f'Your total is ${total:.2f}')

