# Simple Python Script

# Print a greeting
print("Hello! Welcome to the simple Python script.")

# Get user input
name = input("What's your name? ")
print(f"Nice to meet you, {name}!")

# Perform a basic calculation
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}.")
except ValueError:
    print("Please enter valid numbers.")

# Goodbye message
print("Thank you for using the script! Goodbye.")
