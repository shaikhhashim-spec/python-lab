print("Hashim, 251A011")

try:
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numerical values.")

else:
    print(f"The result of division is: {result}")
