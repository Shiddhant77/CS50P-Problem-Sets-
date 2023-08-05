import sys


def main():
    total_line = file_path()
    print(f"There is total number of {len(total_line)} lines in meal.py")


def file_path():
    file_add = []
    try:
        file_name = sys.argv[1]
        if file_name[-3::] != '.py':
            sys.exit(f"Wrong file extension excepted .py got {file_name[-3::]}")
        if sys.argv[1] == '':
            sys.exit("Missing sys argument !")
        with open(file_name, 'r') as file:
            file = file.readlines()
            for line in file:
                if line.startswith('#') or line.startswith("'''"):
                    continue
                if line.isspace():
                    continue
                else:
                    file_add.append(line + '\n')
    except FileNotFoundError:
        sys.exit("File does not exists! ")
    return file_add

if __name__ == '__main__':
    main()

