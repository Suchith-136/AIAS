class student_info:
    def __init__(self):
        self.name = input("Enter name: ")
        self.rollno = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")
    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'  
        else:
            return 'F'
    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}, Grade: {self.grade()}" 
    def __repr__(self):
        return f"student_info(name={self.name}, rollno={self.rollno}, marks={self.marks})"
    def __eq__(self, other):
        if isinstance(other, student_info):
            return self.rollno == other.rollno
        return False
    def __lt__(self, other):
        if isinstance(other, student_info):
            return self.marks < other.marks
        return NotImplemented

if __name__ == "__main__":
    print("Please enter the student details:")
    student = student_info()
    student.display()
    print("Grade:", student.grade())

