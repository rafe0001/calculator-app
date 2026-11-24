print("simple calculator")

while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while True:
    operation = input("Enter operation (+,-,*,/): ")
    if operation in ['+', '-', '*', '/']:
        break
    else:
        print("Invalid operation. Please enter one of +, -, *, /.")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:     
        print("Invalid input. Please enter a numeric value.")

if operation == "+":
    result = num1 + num2
    print("Result: ", result)
elif operation == "-":
    result = num1 - num2
    print("Result: ", result)
elif operation == "*":
    result = num1 * num2
    print("Result: ", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
        