def cm_to_inches(cm):
    return cm / 2.54

cm_input = float(input("Enter the centimeters: "))
inches = cm_to_inches(cm_input)
print(f"The {cm_input}cm is {int(round(inches))} inches")
