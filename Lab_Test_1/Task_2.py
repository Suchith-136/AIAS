import re
import random
import string

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.com"

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Generate a random email and add it to a random text
random_email = generate_email()
sample_text = f"This is a sample text with emails: test1@example.com, {random_email}, and another: user2@domain.org."

# Extract emails from the sample text
emails = extract_emails(sample_text)
print("Extracted emails:", emails)
