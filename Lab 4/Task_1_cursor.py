def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year_input = int(input("Enter a year: "))
if is_leap_year(year_input):
    print(f"{year_input} is a leap year.")
else:
    print(f"{year_input} is not a leap year.")
