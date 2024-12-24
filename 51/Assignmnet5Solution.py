def is_palindrome_slicing(input_string):
    return input_string == input_string[::-1]

# Example usage
input_string = "madam"
print(is_palindrome_slicing(input_string))  # Output: True
