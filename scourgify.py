import csv
import sys
new_file_name = sys.argv[2]
def main():
    a = file_input(new_file_name)
    b = new_file(new_file_name,new_list_dict)


field_names = ['first', 'last', 'house']
new_list_dict = []

def file_input(new_file_name):
    file_name = sys.argv[1]    # existing csv file name here
    new_dict = []
    try:
        if len(sys.argv)-1 !=2:
            sys.exit("Please provide both argument !")
        if file_name[-4::] != '.csv' or new_file_name[-4::]!= '.csv':
            sys.exit("Please provide a .csv file")
        with open(file_name,mode='r') as file:
            names = csv.DictReader(file)
            for row in names:
                new_dict = {}
                first, last = row['name'].split(',')
                new_dict['first'] = first
                new_dict['last']= last
                new_dict['house'] = row['house']
                new_list_dict.append(new_dict)
    except FileNotFoundError:
        sys.exit("File not found !")
    return new_list_dict

def new_file(new_file_name, new_dict):
    with open(new_file_name, mode='w', newline='') as new_file:
            name = csv.DictWriter(new_file, fieldnames=field_names)
            name.writeheader()
            name.writerows(new_dict)

if __name__ == '__main__':
    main()