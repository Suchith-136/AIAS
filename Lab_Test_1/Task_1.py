def convert_currency():
    exchange_rates = {
        ('INR', 'USD'): 0.012,    # Rupees to Dollars
        ('INR', 'GBP'): 0.0095,   # Rupees to Pounds
        ('USD', 'EUR'): 0.92,     # Dollars to Euros
        ('USD', 'GBP'): 0.79,     # Dollars to Pounds
        ('EUR', 'INR'): 90.0      # Euros to Rupees
    }

    print("Currency Conversion Options:")
    print("1. Rupees (INR) to Dollars (USD)")
    print("2. Rupees (INR) to Pounds (GBP)")
    print("3. Dollars (USD) to Euros (EUR)")
    print("4. Dollars (USD) to Pounds (GBP)")
    print("5. Euros (EUR) to Rupees (INR)")

    choice = int(input("Enter your choice (1-5): "))
    amount = float(input("Enter the amount to convert: "))

    if choice == 1:
        from_curr, to_curr = 'INR', 'USD'
    elif choice == 2:
        from_curr, to_curr = 'INR', 'GBP'
    elif choice == 3:
        from_curr, to_curr = 'USD', 'EUR'
    elif choice == 4:
        from_curr, to_curr = 'USD', 'GBP'
    elif choice == 5:
        from_curr, to_curr = 'EUR', 'INR'
    else:
        print("Invalid choice.")
        return

    rate = exchange_rates.get((from_curr, to_curr))
    if rate:
        converted = amount * rate
        print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
    else:
        print("Conversion rate not available.")

if __name__ == "__main__":
    convert_currency()