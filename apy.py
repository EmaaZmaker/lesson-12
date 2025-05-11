


# Convert an integer to binary
number = 42
binary_representation = bin(number)
print(binary_representation)  # Output: '0b101010'


# Example 1: Converting a positive integer
positive_number = 10
print(bin(positive_number))  # Output: '0b1010'

# Example 2: Converting a negative integer
negative_number = -10
print(bin(negative_number))  # Output: '-0b1010'

# Example 3: Using the binary representation in calculations
binary_str = bin(5)  # '0b101'
# Removing the '0b' prefix for further processing
binary_without_prefix = binary_str[2:]
print(binary_without_prefix)  # Output: '101'


#The bin() function is particularly useful when you need to perform bitwise operations or when you need to visualize the binary form of numbers for debugging or educational purposes.