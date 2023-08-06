import csv
import sys
from tabulate import tabulate
field_name = ['Sicilian Pizza', 'Small', 'Large']
table =[]
def main():
    file_take = file_input()


def file_input():
    file_name = sys.argv[1]
    try:
        if file_name[-4::] != '.csv':
            sys.exit(f"Expected .csv file but got {file_name[-3::]} ")
        if sys.argv[1] == '':
            sys.exit("File name expected !")

        with open(file_name,'r',newline='') as file:
            menu = csv.DictReader(file)
            for row in menu:
                row_data = []
                for field in field_name:
                    row_data.append(row[field])
                table.append(row_data)
            print(tabulate(table,headers=field_name, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File name does not exits")

    return table

if __name__ == '__main__':
    main()