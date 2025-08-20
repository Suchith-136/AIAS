def collect_and_store_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    filename = f"{name.replace(' ', '_')}_data.txt"
    with open(filename, "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone Number: {phone}\n")
        file.write(f"Address: {address}\n")

    print(f"User data saved to {filename}")

# Example usage:
collect_and_store_user_data()