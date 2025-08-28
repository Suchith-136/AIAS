#Code 1
with open("example.txt", "w") as f:
    f.write("Hello, world!")
#Code2
f1 = open("data1.txt", "w")
f2 = open("data2.txt", "w")

f1.write("First file content\n")
f2.write("Second file content\n")

print("Files written successfully")

#Code3
data = open("input.txt", "r").readlines()
output = open("output.txt", "w")

for line in data:
    output.write(line.upper())

print("Processing done")
#Code4:
f = open("numbers.txt", "r")
nums = f.readlines()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))
f2 = open("squares.txt", "w")
for sq in squares:
    f2.write(str(sq) + "\n")
print("Squares written")