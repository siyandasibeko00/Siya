while True:
    try:
        first_number = float(input("Enter the first number of your calculation: "))
        second_number = float(input("Enter the second number: "))
        operation = input("Enter the calculation operation (+, -, *, /): ")

        if operation == '+':
            result = first_number + second_number
            print(f"{first_number} + {second_number} = {result}")
        elif operation == "-":
            result = first_number - second_number
            print(f"{first_number} - {second_number} = {result}")
        elif operation == "*":
            result = first_number * second_number
            print(f"{first_number} * {second_number} = {result}")
        elif operation == "/":
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}")
        break

    except ValueError:
        print("Oops! Input was invalid, please enter correct number.")

try:

    with open('equations.txt', 'w+') as file:
        file.write(str((first_number))+" "+((operation)+" "+str((second_number)) + " = " + str((result))))

except FileNotFoundError:
     print("The file that you are trying to open does not exist")

finally:
        file.close()