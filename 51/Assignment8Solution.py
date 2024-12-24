n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    # Print spaces for alignment
    print(" " * (n - i) * 2, end="")
    
    # First half: A, B, C, ...
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    
    # Second half: B, A, ...
    for j in range(i - 1, 0, -1):
        print(chr(64 + j), end=" ")
    
    print()  # Move to the next line
