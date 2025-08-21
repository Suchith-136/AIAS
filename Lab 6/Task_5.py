class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid or insufficient funds.")

    def balance(self):
        print(f"Current balance: {self._balance}")

accounts = {}

def create_account():
    username = input("Enter new username: ")
    if username in accounts:
        print("Account already exists.")
        return
    password = input("Enter new password: ")
    accounts[username] = BankAccount(username, password)
    print("Account created successfully.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    account = accounts.get(username)
    if account and account.password == password:
        print("Login successful.")
        account_menu(account)
    else:
        print("Invalid credentials.")

def account_menu(account):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
        choice = input("Choose an option: ")
        if choice == '1':
            account.balance()
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            print("Logged out.")
            break
        else:
            print("Invalid option.")

def main_menu():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()