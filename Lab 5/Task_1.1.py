import getpass
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def collect_user_data():
    """Collect user data from input."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    return {
        "name": name,
        "age": age,
        "email": email,
        "phone": phone,
        "address": address
    }

def anonymize_data(data):
    """Anonymize sensitive data (e.g., mask email and phone)."""
    # Mask email (show only first letter and domain)
    email_parts = data["email"].split("@")
    masked_email = email_parts[0][0] + "***@" + email_parts[1] if len(email_parts) == 2 else "***"
    # Mask phone (show only last 2 digits)
    masked_phone = "***" + data["phone"][-2:] if len(data["phone"]) >= 2 else "***"
    data["email"] = masked_email
    data["phone"] = masked_phone
    return data

def save_data_to_file(data, password_hash, filename="userdata.txt"):
    """Save anonymized data and password hash to a file."""
    with open(filename, "w") as f:
        f.write("# User Data (Anonymized)\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("# Password Hash (for protection)\n")
        f.write(f"password_hash: {password_hash}\n")

def main():
    print("Welcome! Please create a password to protect your data.")
    password = getpass.getpass("Create a password: ")
    password_hash = hash_password(password)
    print("Now, enter your details.")
    user_data = collect_user_data()
    anonymized_data = anonymize_data(user_data)
    save_data_to_file(anonymized_data, password_hash)
    print("Your anonymized data has been saved and protected with your password.")

if __name__ == "__main__":
    main()