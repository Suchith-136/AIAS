def is_palindrome(s):
    return s == s[::-1]

def run_tests():
    test_cases = [
        ("madam", True),
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("a", True),
        ("abcba", True),
        ("abccba", True),
        ("ab", False)
    ]
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        print(f"Test case {i}: Input='{input_str}' | Expected={expected} | Got={result} | {'PASS' if result == expected else 'FAIL'}")

def main():
    user_input = input("Enter a string to check if it's a palindrome: ")
    print("Result:", is_palindrome(user_input))
    print("\nRunning test cases:")
    run_tests()

if __name__ == "__main__":
    main()