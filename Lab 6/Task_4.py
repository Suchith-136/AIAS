def sum_to_n():
    # Take input from the user and convert it to integer
    n = int(input("Enter a positive integer n: "))
    
    # Calculate the sum of first n natural numbers using the formula n*(n+1)//2
    total = n * (n + 1) // 2
    
    # Print the result
    print(f"The sum of first {n} numbers is: {total}")

# Call the function
sum_to_n()