def format_full_name():
    first_name = input("Enter the first name: ").strip()
    last_name = input("Enter the last name: ").strip()
    full_name = f"{first_name} {last_name}"
    print("Full name:", full_name)

if __name__ == "__main__":
    format_full_name()