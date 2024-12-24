def print_pattern_recursive(n, i=1):
    if i > n:
        return
    print(' '.join(['*'] * i))
    print_pattern_recursive(n, i + 1)

# Example usage
n = 4
print_pattern_recursive(n)
