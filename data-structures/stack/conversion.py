
import stack

# Basic method to convert a decimal number to binary
def decimal_to_binary(decimal_number):
    remaining_stack = stack.Stack()

    while decimal_number > 0:
        remaining = decimal_number % 2
        remaining_stack.push(remaining)
        decimal_number //= 2

    binary_string = ""
    while not remaining_stack.empty():
        binary_string = binary_string + str(remaining_stack.pop())

    return binary_string

def base_converter(decimal_number, base):
    digits = "0123456789ABCDEF"
    remaining_stack = stack.Stack()

    while (decimal_number > 0):
        remaining = decimal_number % base
        remaining_stack.push(remaining)
        decimal_number //= base

    output_string = ""
    while not remaining_stack.empty():
        output_string += digits[remaining_stack.pop()]

    return output_string
