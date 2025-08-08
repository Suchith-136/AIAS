def find_largest_of_three():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    largest = max(num1, num2, num3)
    return largest

# Example usage
numbers = []
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("The largest number is:", max(numbers))