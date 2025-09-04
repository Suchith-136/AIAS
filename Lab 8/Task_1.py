def is_valid_email(email: str) -> bool:
    # Check for exactly one '@'
    if not isinstance(email, str) or email == "":
        return False
    if email.count('@') != 1:
        return False
    # Must contain at least one '.'
    if '.' not in email:
        return False
    # Must not start or end with special characters
    special_chars = {'@', '.'}
    if email[0] in special_chars or email[-1] in special_chars:
        return False
    # '@' and '.' must not be adjacent or doubled
    if '..' in email or '.@' in email or '@.' in email:
        return False
    return True


def main() -> None:
    user_email = input("Enter an email address: ")
    if is_valid_email(user_email):
        print("Valid email address.")
    else:
        print("Invalid email address.")


if __name__ == "__main__":
    main()
