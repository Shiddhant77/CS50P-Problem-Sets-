def main():
    fraction = input("Enter the number in x/y format : ")
    number = convert(fraction)
    fuel = gauge(number)
    print(f"You have total number of {number}% fuel remaining")
    print(f"You have around {fuel} remaining")

def convert(fraction):
    while True:
        try:
            x,y = map(int, fraction.split('/'))
            if x > y:
                raise ValueError("Please enter correct value")
            if y == 0:
                raise ZeroDivisionError("Y should not be 0")
        except ValueError:
            print("Please enter correct value")
            break

        else:
            return (x/y)*100


def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    elif percentage >=2 and percentage<=98:
        return f'{percentage}%'
    else:
        raise ValueError("Number out of range")


if __name__ == "__main__":
    main()