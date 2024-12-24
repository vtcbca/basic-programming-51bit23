def factorial_using_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_using_loop(number)}")
