def get_square_matrix():
    while True:
        try:
            n = int(input("Enter the order of the square matrix (N): "))
            if n <= 0:
                print("Order must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print(f"Enter the elements of the {n}x{n} matrix row-wise (space separated):")
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            if len(row_input) != n:
                print(f"Please enter exactly {n} elements.")
                continue
            try:
                row = [int(x) if x.lstrip('-').isdigit() else x for x in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid elements.")
    return matrix

def rotate_matrix_90_clockwise(matrix):
    # Do not modify input
    n = len(matrix)
    rotated = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = matrix[i][j]
    return rotated

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))

def compare_lists(old, new):
    added = [x for x in new if x not in old]
    removed = [x for x in old if x not in new]
    return added, removed

def agritech():
    matrix = get_square_matrix()
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    rotated = rotate_matrix_90_clockwise(matrix)
    print("\nMatrix after 90° clockwise rotation:")
    print_matrix(rotated)

    # Ask user if they want to compare two lists for added/removed
    resp = input("\nDo you want to compare two lists for added/removed elements? (y/n): ").strip().lower()
    if resp == 'y':
        def parse_list_input(prompt):
            while True:
                s = input(prompt).strip()
                if s.startswith('[') and s.endswith(']'):
                    s = s[1:-1]
                items = [x.strip() for x in s.split(',') if x.strip()]
                # Try to convert to int if possible
                parsed = []
                for x in items:
                    if x.lstrip('-').isdigit():
                        parsed.append(int(x))
                    else:
                        parsed.append(x)
                return parsed
        old = parse_list_input("Enter old list (e.g. ['a','b','c'] or [1,2,3]): ")
        new = parse_list_input("Enter new list (e.g. ['b','c','d'] or [2,3,4]): ")
        added, removed = compare_lists(old, new)
        print(f"added={added}, removed={removed}")

if __name__ == "__main__":
    agritech()
