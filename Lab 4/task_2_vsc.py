def cm_to_inches(cm):
    inches = cm / 2.54
    return round(inches)

if __name__ == "__main__":
    cm = float(input("Enter the centimeters: "))
    inches = cm_to_inches(cm)
    print(f"The {cm}cm is {inches} inches")