def count_vowels():
    s = input("Enter the string: ")
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print(f"The no. of vowels in the string: {count}")

count_vowels()