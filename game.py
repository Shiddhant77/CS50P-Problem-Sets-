import  random

n= input("Please select difficulty level : Easy, Medium , Hard ").lower()
attempts = 0
if n == "easy" or n == "e":
    correct_num = random.randint(1, 20)
elif n == "medium" or n == "m":
    correct_num = random.randint(1, 50)
else:
    correct_num = random.randint(1, 100)

while True:
    try:

        guess = (int(input("Enter you guess number : ")))
        if guess <=0:
            print("Please enter number higher than 0 ")
    except ValueError:
        attempts+=1
        print("Please enter a valid number")
        continue

    if guess > correct_num:
        attempts += 1
        print("To large !!")

    elif guess < correct_num:
        attempts += 1
        print("To Small")

    elif guess == correct_num:
        attempts += 1
        print(f"Wow! Congratulations, You have guessed the correct number on {attempts} attempts")
        break

