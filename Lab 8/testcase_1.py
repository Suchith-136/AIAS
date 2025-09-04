import unittest
from Task_1 import is_valid_email
import re

class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("john.doe123@domain.co"))

    def test_missing_at_symbol(self):
        self.assertFalse(is_valid_email("userexample.com"))
        self.assertFalse(is_valid_email("user.example.com"))

    def test_multiple_at_symbols(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("user@ex@ample.com"))

    def test_starts_with_special_character(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("_user@example.com"))
        self.assertFalse(is_valid_email("-user@example.com"))

    def test_ends_with_special_character(self):
        self.assertFalse(is_valid_email("user.@example.com"))
        self.assertFalse(is_valid_email("user_@example.com"))
        self.assertFalse(is_valid_email("user-@example.com"))

    def test_empty_string(self):
        self.assertFalse(is_valid_email(""))

    def test_only_at_symbol(self):
        self.assertFalse(is_valid_email("@"))

    def test_no_characters_before_at(self):
        self.assertFalse(is_valid_email("@example.com"))

    def test_no_characters_after_at(self):
        self.assertFalse(is_valid_email("user@"))

if __name__ == "__main__":
    unittest.main()
# Task_1.py


def is_valid_email(email):
    # Must contain exactly one @
    if email.count('@') != 1:
        return False
    # Must not start or end with special characters
    if re.match(r'^[\W_]', email) or re.match(r'[\W_]$', email):
        return False
    # Must contain characters before and after @
    local, domain = email.split('@')
    if not local or not domain:
        return False
    # Must contain only allowed characters
    if not re.match(r'^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+$', email):
        return False
    return True

if __name__ == "__main__":
    email = input("Enter an email to validate: ")
    print("Valid" if is_valid_email(email) else "Invalid")