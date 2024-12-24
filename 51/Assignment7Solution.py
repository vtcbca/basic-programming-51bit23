n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    print(" " * (n - i) * 2, end="")  # Add spaces for alignment
    for j in range(1, 2 * i):
        print(j, end=" ")
    print()  # Move to the next line
