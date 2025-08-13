def count_lines_in_file():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            print(f"The no. of lines in the file are {len(lines)} lines")
    except FileNotFoundError:
        print("File not found.")

count_lines_in_file()
