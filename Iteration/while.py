enter_number = 0

user_number = int(input("Please enter a number of your choice: (Zero value is invalid)"))

if user_number == 0:
    print("Input invalid")

while user_number != -1:
    enter_number += user_number

    user_number = int(input("Please enter a number of your choice: (Zero value is invalid) "))

    if user_number == 0:
        print("Input invalid")

    if user_number == -1:
        print(enter_number)
        break