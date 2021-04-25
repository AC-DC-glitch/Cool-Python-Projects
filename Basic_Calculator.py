import math
from math import*


def calculator():
    operation = input(
        "Enter the operation you want to be carried out.\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. First number raised to second\n6. Sine of an angle\n7. Cosine of an angle\n8. Tangent of an angle\n Enter here: ")
    try:
        if operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5":
            num1 = float(input("Input the first number: "))
            num2 = float(input("Input the second number: "))

            if operation == "1":
                if num1 == 2.0 and num2 == 2.0:
                    return 5
                return num1 + num2
            elif operation == "2":
                return num1 - num2
            elif operation == "3":
                return num1 * num2
            elif operation == "4":
                return num1 / num2
            elif operation == "5":
                return pow(num1, num2)
    except ValueError:
        print("Invalid Input")
    except ZeroDivisionError:
        print("Err_Divided_by_zero")

    try:
        if operation == "6" or operation == "7" or operation == "8":
            num_a = float(input("Input a number:"))

            if operation == "6":
                return math.sin(math.radians(num_a))
            elif operation == "7":
                return math.cos(math.radians(num_a))
            elif operation == "8":
                return math.tan(math.radians(num_a))
    except ValueError:
        print("Invalid Input")


print(calculator())
