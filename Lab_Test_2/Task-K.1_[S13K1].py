def rotate_matrix(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(str(x) for x in row))

def agritech():
    try:
        n = int(input("Enter the order of the square matrix (N): "))
        if n <= 0:
            print("Order must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    print(f"Enter the elements of the {n}x{n} matrix row-wise (space separated):")
    matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            if len(row_input) != n:
                print(f"Please enter exactly {n} elements.")
                continue
            try:
                row = [int(x) for x in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid integers.")

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    rotate_matrix(matrix)

    print("\nMatrix after 90° clockwise rotation:")
    print_matrix(matrix)

if __name__ == "__main__":
    agritech()
