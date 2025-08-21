def num_table(num):
    print(f"Multiplication table of {num}:")
    i = 1
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1

if __name__ == "__main__":
    num = int(input("Enter a number to print its multiplication table: "))
    num_table(num)
