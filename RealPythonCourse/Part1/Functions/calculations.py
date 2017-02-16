def square_number(number):
    sqr_num = number ** 2
    return sqr_num

input_num = 5
output_num = square_number(input_num)
print(output_num)

def return_difference(num1, num2):
    """Return the difference between two numbers. Subtracts n2 from n1."""

    difference = num1 - num2
    return difference

output_diff = return_difference(5, 3)
print(output_diff)

def return_sum(num1, num2):
    total_sum = num1 + num2
    return total_sum

output_sum = return_sum(5, 3)
print(output_sum)
print(help(return_difference))
