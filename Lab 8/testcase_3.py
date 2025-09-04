import re
from Task_3 import is_palindrome

def is_sentence_palindrome(sentence):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    return is_palindrome(cleaned)

def test_is_sentence_palindrome():
    test_cases = [
        ("A man a plan a canal Panama", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("Eva, can I see bees in a cave?", True),
        ("Madam In Eden, I'm Adam", True),
        ("Never odd or even", True),
        ("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.", True),
        ("Hello, World!", False),
        ("This is not a palindrome.", False),
        ("", True),
        ("Able was I, I saw Elba", True),
        ("Step on no pets", True),
        ("Red roses run no risk, sir, on Nurse's order.", True),
        ("Palindrome", False),
        ("Was it a car or a cat I saw", True),
    ]
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = is_sentence_palindrome(sentence)
        assert result == expected, f"Test case {i} failed: Input='{sentence}' | Expected={expected} | Got={result}"

if __name__ == "__main__":
    test_is_sentence_palindrome()
    print("All tests passed.")