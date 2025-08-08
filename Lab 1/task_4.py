class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

students = []
n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    marks = float(input("Marks: "))
    student = Student(name, roll_no, marks)
    students.append(student)

print("\nStudent Details:")
for student in students:
    student.display()