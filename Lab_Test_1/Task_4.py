import csv

def read_students_from_csv(filename):
    students = {}
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name'].strip()
            roll_no = row['Roll.no'].strip()
            try:
                maths = float(row['Maths marks'])
                physics = float(row['Physics marks'])
                chemistry = float(row['Chemistry marks'])
            except ValueError:
                # Skip rows with invalid marks
                continue
            total = maths + physics + chemistry
            average = total / 3
            students[name.lower()] = {
                'Name': name,
                'Roll.no': roll_no,
                'Maths': maths,
                'Physics': physics,
                'Chemistry': chemistry,
                'Total': total,
                'Average': average
            }
    return students

def main():
    filename = input("Enter the CSV filename: ").strip()
    try:
        students = read_students_from_csv(filename)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return

    if not students:
        print("No valid student data found in the file.")
        return

    while True:
        print("\nAvailable students:")
        for student in students.values():
            print(f"- {student['Name']} (Roll No: {student['Roll.no']})")
        student_name = input("\nEnter the student's name to view marks (or type 'exit' to quit): ").strip().lower()
        if student_name == 'exit':
            break
        if student_name not in students:
            print("Student not found. Please try again.")
            continue

        choice = input("Type 'total' to see total marks or 'average' to see average marks: ").strip().lower()
        if choice == 'total':
            print(f"Total marks for {students[student_name]['Name']}: {students[student_name]['Total']}")
        elif choice == 'average':
            print(f"Average marks for {students[student_name]['Name']}: {students[student_name]['Average']:.2f}")
        else:
            print("Invalid choice. Please type 'total' or 'average'.")

if __name__ == "__main__":
    main()



