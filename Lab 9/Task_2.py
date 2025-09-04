class student:
    """
    A class to represent a student and manage their fee payment status.
    Attributes:
        name (str): The name of the student.
        hostel_status (str): The hostel status of the student (e.g., 'Hosteller', 'Day Scholar').
        roll_no (str): The roll number of the student.
        fee_paid (int): The total fee amount paid by the student.
    Methods:
        __init__(name, hostel_status, roll_no):
            Initializes a student object with name, hostel status, roll number, and sets fee_paid to 0.
        fee_update(amount):
            Adds the specified amount to the student's total fee paid.
        display():
            Prints the student's details including name, roll number, hostel status, and total fee paid.
    """

    def __init__(self, name, hostel_status, roll_no):
        self.name = name                   # Store student name
        self.hostel_status = hostel_status # Store student roll number
        self.roll_no = roll_no             # Store student hostel status
        self.fee_paid = 0                  # Initialize fee paid to 0
    
    def fee_update(self, amount):
        self.fee_paid += amount            # Update the fee paid by adding the amount
    
    def display(self):
        print("\n--- Student Details ---")
        print("Student Name:", self.name)       # Print student name   
        print("Roll Number:", self.roll_no)     # Print student roll number
        print("Hostel Status:", self.hostel_status)  # Print hostel status
        print("Total Fee Paid:", self.fee_paid)    # Print total fee paid

name = input("Enter student name: ")                # Input student name
hostel_status = input("Enter hostel status (Yes/No): ")# Input hostel status
roll_no = int(input("Enter roll number: "))# Input roll number
student1 = student(name, hostel_status, roll_no)# Create a student object

fee = int(input("Enter fee amount to update: "))  # Input fee amount to update
student1.fee_update(fee)              # Update the fee paid
student1.display()                  # Display student details