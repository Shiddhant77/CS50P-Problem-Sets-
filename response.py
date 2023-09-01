import validators


def main():
    try:
        email_address = input("Please enter a valid email address : ")
        if validators.email(email_address) == True:
            print("Valid")
        else:
            print("I AIN'T WORKING AGAIN ")
    except Exception:
        print("Enter a valid email address")


if __name__ == "__main__":
    main()
