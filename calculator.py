# Asking the user for the first number
num1 = float(input("Enter first number: "))

# Asking the user for the second number
num2 = float(input("Enter second number: "))

# Asking the user for the mathematical operation
operation = input("Enter operation (+, -, *, /): ")

# Performing the operation based on user input
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
