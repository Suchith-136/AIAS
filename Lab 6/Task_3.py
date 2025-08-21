# Program to classify age groups using nested if-elif-else statements

# Take age input from the user
age = int(input("Enter your age: "))

# Check if age is valid (non-negative)
if age >= 0:
    # Nested conditional statements to classify age groups
    if age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teenager.")
    elif age <= 59:
        print("You are an adult.")
    else:
        print("You are an old age person.")
else:
    # Handle invalid age input
    print("Invalid age entered. Age cannot be negative.")

# Explanation:
# - The outer if checks for valid age input.
# - The nested if-elif-else checks the age range and prints the corresponding group.
# - elif is used for multiple conditions.
# - else handles ages 60 and above.