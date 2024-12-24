from functools import reduce

def reverse_string_reduce(input_string):
    return reduce(lambda x, y: y + x, input_string)

# Example usage
input_string = "Hello, World!"
print(reverse_string_reduce(input_string))
