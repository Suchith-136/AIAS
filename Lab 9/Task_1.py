def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.
    Args:
        numbers (list of int): A list of integers to be processed.
    Returns:
        tuple: A tuple containing two integers:
            - The sum of all even numbers in the list.
            - The sum of all odd numbers in the list.
    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
    """

    even_sum = 0  # Initialize sum for even numbers
    odd_sum = 0   # Initialize sum for odd numbers
    for num in numbers:  # Iterate through each number in the list
        if num % 2 == 0:  # Check if the number is even
            even_sum += num  # Add to even sum if even
        else:
            odd_sum += num  # Add to odd sum if odd
    return even_sum, odd_sum  # Return the tuple of even and odd sums

if __name__ == "__main__":  # Check if the script is run directly
    nums = list(map(int, input("Enter numbers separated by space: ").split()))  # Take input and convert to list of integers
    even_sum, odd_sum = sum_even_odd(nums)  # Call the function to get sums
    print(f"Sum of even numbers: {even_sum}")  # Print sum of even numbers
    print(f"Sum of odd numbers: {odd_sum}")  # Print sum of odd numbers