"""
Calculator Module
=================
This module provides basic calculator functions: addition, subtraction,
multiplication, and division. The program takes user input from the console
and performs the selected operation.
"""
def add(a, b):       # Addition function
    return a + b   # Return the sum of a and b

def subtract(a, b):   # Subtraction function
    return a - b     # Return the difference of a and b

def multiply(a, b):  # Multiplication function
    return a * b     # Return the product of a and b

def divide(a, b):     # Division function
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")    # Handle division by zero
    return a / b

if __name__ == "__main__":         # Main program execution
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")      # Take user choice input

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == "1":                            # Addition
        print("Result:", add(x, y))
    elif choice == "2":                # Subtraction
        print("Result:", subtract(x, y))
    elif choice == "3":                    # Multiplication
        print("Result:", multiply(x, y))
    elif choice == "4":                        # Division
        try:
            print("Result:", divide(x, y))  # Handle potential division by zero
        except ZeroDivisionError as e:        
            print("Error:", e)                   # Print error message
    else:
        print("Invalid choice!")
