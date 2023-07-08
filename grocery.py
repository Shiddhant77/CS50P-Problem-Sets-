# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.



list_item=[]
my_dict = {}
while True:
    try:
        item = input("Enter an item : ").upper()
        list_item.append(item)

    except EOFError:
        print("Thank you for ordering!")
        break

for i in list_item:
    if i in my_dict:
        my_dict[i] +=1
    else:
        my_dict[i] = 1

sorted_items = sorted(my_dict.keys())

for item in sorted_items:
    count = my_dict[item]
    print(f'{count} {item}')
